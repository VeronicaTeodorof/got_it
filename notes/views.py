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
    # Instantiate the form with the fetched source
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
    # unbound form
    form = UnitForm(source=current_source)
    forms = [UnitForm(instance=unit, source=current_source) for unit in units]
    unit_forms = list(zip(units, forms))
    return render(request,
                  "notes/source_detail.html",
                  {"current_source": current_source,
                   "unit_forms": unit_forms,
                   "units": units,
                   "form": form
                   })


@login_required
def edit_unit(request, source_pk, unit_pk):
    """
    View for the edit unit form
    """
    current_source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=current_source)
    form = UnitForm(instance=unit, current_source=current_source)
    return render(
        request,
        'notes/source_detail.html',
        {'current_source': current_source, 'unit': unit, 'form': form}
    )


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
    return render(request,
                  'notes/unit_detail.html',
                  {'source': source, 'unit': unit})
