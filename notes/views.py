from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Source, Unit
from .forms import SourceForm, UnitForm


# Create your views here.

# --- Home ---
def home(request):
    return render(request, 'notes/index.html')


# --- Dashboard/ Sources ---
# Prevent browser caching
# so back button forces a fresh server request after logout
@never_cache
@login_required
def dashboard(request):
    """
    Retrieve and display a list of sources belonging to the current user,
    and create source form
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        # user=request.user is passed in as a keyword argument because
        # there are many optional arguments that could be passed and here those
        # ones are skipped
        form = SourceForm(request.POST, user=request.user)
        # check whether it's valid:
        if form.is_valid():
            source = form.save(commit=False)
            source.user = request.user
            source.save()
            return redirect('source-detail', source_pk=source.pk)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SourceForm(user=request.user)
    # Filter by user first, then order —
    # chained to avoid overwriting the user filter
    sources = Source.objects.filter(user=request.user).order_by(
        '-source_creation_date'
        )
    # Creates a list of prepopulated forms, one per source
    forms = [SourceForm(instance=source) for source in sources]
    # Creates a list of source, form tuples
    # pairing each source with its corresponding prepopulated form
    # to be passed to the context
    source_forms = list(zip(sources, forms))
    return render(
        request,
        'notes/dashboard.html',
        {'form': form, 'sources': sources, 'source_forms': source_forms}
        )


@login_required
def edit_source(request, source_pk):
    """ View for the edit source form"""
    # Retrieve the specific record from the database using the pk
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    if request.method == 'POST':
        # Bind the submitted data to the form in the POST block
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        return render(
            request,
            'notes/dashboard.html',
            {'form': form, 'source': source}
            )
    # GET fallback in this view is never actually reached,
    # handled by dashboard view
    # left for readability and eventual UI changes
    form = SourceForm(instance=source)
    return render(
        request,
        'notes/dashboard.html',
        {'form': form, 'source': source}
        )


@login_required
def delete_source(request, source_pk):
    """View for deleteSourceModal
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    if request.method == 'POST':
        source.delete()
        messages.success(request, "Source deleted successfully!")
    return redirect('dashboard')


# --- Source detail/Units ---
@login_required
def source_detail(request, source_pk):
    """
    Retrieve and display a single source belonging to the current user
    and a list of its units.
    """
    current_source = get_object_or_404(Source, pk=source_pk, user=request.user)
    units = Unit.objects.filter(source=current_source).order_by(
        'unit_last_modified_date'
    )
    if request.method == 'POST':
        # a bound copy of the form is created with
        # request.POST being passed to this copy
        form = UnitForm(request.POST, source=current_source)
        # is_valid() triggers field-level then form-level cleaning.
        if form.is_valid():
            unit = form.save(commit=False)
            unit.source = current_source
            unit.save()
            return redirect('unit-detail',
                            source_pk=current_source.pk,
                            unit_pk=unit.pk
                            )
        else:
            return render(request,
                          "notes/source_detail.html",
                          {"current_source": current_source,
                           "units": units,
                           "form": form
                           })
    # unbound form, passed as form in context for create unit form
    form = UnitForm(source=current_source)
    # creates a list of prepopulated edit forms, one for each unit, but not yet
    # paired with its respective unit
    forms = [UnitForm(instance=unit, source=current_source) for unit in units]
    # pairs each unit with its corresponding form;
    # prepopulated forms are always present on the page
    # passed in context as unit_forms
    unit_forms = list(zip(units, forms))
    return render(request,
                  "notes/source_detail.html",
                  {"current_source": current_source,
                   "unit_forms": unit_forms,
                   "units": units,
                   "form": form
                   })


# while source_detail view can handle displaying both create and edit forms
# it needs to distinguish between POST requests for create and POST requests
# for edit
# the solution here was to create a separate view to handle POST requests for
# edit unit form, leaving source_detail view to handle only the POST requests
# for create unit form
@login_required
def edit_unit(request, source_pk, unit_pk):
    """
    View for the POST branch of the edit unit form
    """
    # the view has to first run its security checks and fetch the required
    # objects to bind to the new form if they exists
    # takes source_pk argument and has to see whether it exists or not
    # goes to Source table, checks the indicated pk exists, checks the user
    # is the one that made the request
    # fetches object if it passes security checks
    # returns 404 otherwise
    current_source = get_object_or_404(
        Source, pk=source_pk, user=request.user
        )
    # now takes unit_pk argument and checks whether it exists or not
    # goes to Unit table, checks the indicated pk exists, checks it
    # belongs to the source indicated in current_source
    # fetches or returns 404
    unit = get_object_or_404(Unit, pk=unit_pk, source=current_source)
    # now you want the view to make a copy or the UnitForm and attach
    # to it data received in request.POST
    # you take a copy of the UnitForm and with instance=unit you tell
    # Django that in the previously fetched unit record you want the
    # data from request.POST, not the old data
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit, source=current_source)
        if form.is_valid():
            form.save()
            return redirect('source-detail', source_pk=current_source.pk)
        units = Unit.objects.filter(source=current_source).order_by(
            'unit_last_modified_date')
        # for each unit in the list, if the pk matches the one that just
        # failed, respective form is brought back with errors intace,
        # all other ones are given fresh prepopulated forms as normal
        forms = [
            form if u.pk == unit.pk
            else UnitForm(instance=u, source=current_source)
            for u in units
        ]
        unit_forms = list(zip(units, forms))
        return render(request,
                      'notes/source_detail.html',
                      {"current_source": current_source,
                       "unit_forms": unit_forms,
                       "units": units,
                       "form": UnitForm(source=current_source),
                       'failed_unit_pk': unit_pk})

    # GET fallback - never actually reached,
    # edit forms are pre-rendered in source_detail view
    # left for readability and eventual UI changes
    form = UnitForm(instance=unit, source=current_source)
    return render(request,
                  'notes/source_detail.html',
                  {"current_source": current_source,
                   "units": Unit.objects.filter(
                       source=current_source).order_by(
                       'unit_last_modified_date'),
                   "form": UnitForm(source=current_source)})


@login_required
def delete_unit(request, source_pk, unit_pk):
    """View for deleting units"""
    current_source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=current_source)
    if request.method == 'POST':
        unit.delete()
        messages.success(request, "Uni deleted successfully!")
    return redirect('source-detail', source_pk=source_pk)


# --- Unit detail/Notes ---
@login_required
def unit_detail(request, source_pk, unit_pk):
    """Retrieve and display a single unit belonging to a source
    and a list of all related notes
    """
    unit = get_object_or_404(Unit,
                             pk=unit_pk,
                             source__pk=source_pk,
                             source__user=request.user
                             )
    source = unit.source
    references = unit.reference_notes.all()
    return render(request,
                  'notes/unit_detail.html',
                  {'source': source,
                   'unit': unit,
                   'references': references})
