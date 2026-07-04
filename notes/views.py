from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Source, Unit, Reference
from .forms import SourceForm, UnitForm, ReferenceForm


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
            messages.success(request, "Source added.")
            return redirect('dashboard')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SourceForm(user=request.user)
    # Filter by user first, then order —
    # chained to avoid overwriting the user filter
    sources = Source.objects.filter(user=request.user).order_by(
        '-source_creation_date'
        )
    paginator = Paginator(sources, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'notes/dashboard.html',
        {'form': form, 'sources': sources,
         "page_obj": page_obj}
        )


@login_required
def delete_source(request, source_pk):
    """View for deleteSourceModal
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    if request.method == 'POST':
        source.delete()
        messages.success(request, "Source deleted.")
    return redirect('dashboard')


# --- Source detail/Units ---
@login_required
def source_detail(request, source_pk):
    """
    Retrieve, display, and edit a single source belonging to the current user,
    list its units, and handle both the source-edit form and the add-unit
    form, distinguished via the 'form_type' hidden field.
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    units = Unit.objects.filter(source=source).order_by(
        'unit_last_modified_date'
    )
    paginator = Paginator(units, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    edit_mode = False

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'edit_source':
            form = SourceForm(request.POST, instance=source, user=request.user)
            unit_form = UnitForm(source=source)
            if form.is_valid():
                form.save()
                return redirect('source-detail', source_pk=source.pk)
            edit_mode = True

        elif form_type == 'add_unit':
            form = SourceForm(instance=source, user=request.user)
            unit_form = UnitForm(request.POST, source=source)
            if unit_form.is_valid():
                unit = unit_form.save(commit=False)
                unit.source = source
                unit.save()
                messages.success(request, "Unit added.")
                return redirect('source-detail', source_pk=source.pk)

        else:
            form = SourceForm(instance=source, user=request.user)
            unit_form = UnitForm(source=source)

    else:
        form = SourceForm(instance=source, user=request.user)
        unit_form = UnitForm(source=source)
        edit_mode = request.GET.get('edit') == '1'

    return render(request, 'notes/source_detail.html', {
        'source': source,
        'units': units,
        'form': form,
        'unit_form': unit_form,
        'edit_mode': edit_mode,
        'page_obj': page_obj
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
        messages.success(request, "Unit deleted successfully!")
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
    references = unit.reference_notes.all().order_by('-last_modified_date')
    return render(request,
                  'notes/unit_detail.html',
                  {'source': source,
                   'unit': unit,
                   'references': references})


# --- Reference Notes ---
@login_required
def reference_detail(request, source_pk, unit_pk, reference_pk):
    """Retrieve and display a single reference"""
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)
    reference = get_object_or_404(Reference, pk=reference_pk, unit=unit)
    return render(request,
                  'notes/reference_detail.html',
                  {'source': source,
                   'unit': unit,
                   'reference': reference}
                  )


@login_required
def create_reference(request, source_pk, unit_pk):
    """
    Create reference notes
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.unit = unit
            reference.save()
            messages.success(request, "Reference note saved.")
            return redirect('unit-detail', source_pk, unit_pk)
        return render(request,
                      'notes/create_reference.html',
                      {'source': source,
                       'unit': unit,
                       'form': form}
                      )
    form = ReferenceForm()
    return render(request,
                  'notes/create_reference.html',
                  {'source': source,
                   'unit': unit,
                   'form': form}
                  )


@login_required
def edit_reference(request, source_pk, unit_pk, reference_pk):
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)
    reference = get_object_or_404(Reference, pk=reference_pk, unit=unit)
    if request.method == 'POST':
        form = ReferenceForm(
            request.POST, instance=reference, unit=unit)
        if form.is_valid():
            reference = form.save()
            return redirect(
                'reference-detail', source_pk, unit_pk, reference_pk
                )
        return render(request,
                      'notes/edit_reference.html',
                      {'source': source,
                       'unit': unit,
                       'reference': reference,
                       'form': form
                       })
    form = ReferenceForm(instance=reference, unit=unit)
    return render(request,
                  'notes/edit_reference.html',
                  {'source': source,
                   'unit': unit,
                   'reference': reference,
                   'form': form})
