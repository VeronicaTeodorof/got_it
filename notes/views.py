from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Source, Unit, Reference, MyWords, Question
from .forms import SourceForm, UnitForm, ReferenceForm, MyWordsForm
from .forms import QuestionForm


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
    # True when navigating here from the sidebar's "Add source" link,
    # so the create-source form renders already expanded (?add_source=open
    add_source_open = request.GET.get('add_source') == 'open'
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
         "page_obj": page_obj,
         "add_source_open": add_source_open}
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
    add_unit_open = request.GET.get('add_unit') == 'open'
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    sources = Source.objects.filter(user=request.user)
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
        'sources': sources,
        'units': units,
        'form': form,
        'unit_form': unit_form,
        'edit_mode': edit_mode,
        'page_obj': page_obj,
        'add_unit_open': add_unit_open,
    })


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
    """Retrieve and display a single unit belonging to a source,
    handle inline editing of the unit's own fields, and display
    related notes.
    """
    unit = get_object_or_404(Unit,
                             pk=unit_pk,
                             source__pk=source_pk,
                             source__user=request.user)
    source = unit.source
    references = unit.reference_notes.all().order_by('-last_modified_date')
    mywords = unit.mywords_notes.all().order_by('-last_modified_date')
    questions = unit.question_notes.all().order_by('-last_modified_date')

    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit, source=source)
        if form.is_valid():
            form.save()
            # PRG pattern: redirect back to this same page after success
            return redirect('unit-detail',
                            source_pk=source.pk,
                            unit_pk=unit.pk)
        # invalid: re-render with errors, still in edit mode
        return render(request,
                      'notes/unit_detail.html',
                      {'source': source,
                       'unit': unit,
                       'references': references,
                       'form': form,
                       'edit_mode': True})

    edit_mode = request.GET.get('edit') == '1'
    form = UnitForm(instance=unit, source=source) if edit_mode else None
    return render(request,
                  'notes/unit_detail.html',
                  {'source': source,
                   'unit': unit,
                   'references': references,
                   'mywords': mywords,
                   'questions': questions,
                   'form': form,
                   'edit_mode': edit_mode})


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
                   'reference': reference,
                   'in_note_view': True}
                  )


@login_required
def create_reference(request, source_pk, unit_pk):
    """
    Create reference notes
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)
    next_url = request.GET.get('next')

    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.unit = unit
            reference.save()
            messages.success(request, "Reference note saved.")
            return redirect('reference-detail',
                            source_pk,
                            unit_pk,
                            reference.pk
                            )
    else:
        form = ReferenceForm()

    return render(request,
                  'notes/create_reference.html',
                  {'source': source,
                   'unit': unit,
                   'form': form,
                   'in_note_view': True,
                   'next_url': next_url}
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
                       'form': form,
                       'in_note_view': True
                       })
    form = ReferenceForm(instance=reference, unit=unit)
    return render(request,
                  'notes/edit_reference.html',
                  {'source': source,
                   'unit': unit,
                   'reference': reference,
                   'form': form,
                   'in_note_view': True})


# --- Question Notes ---
@login_required
def question_detail(request, source_pk, unit_pk, question_pk):
    """Retrieve and display a single Question note"""
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)
    question = get_object_or_404(Question, pk=question_pk, unit=unit)
    return render(request,
                  'notes/question_detail.html',
                  {'source': source,
                   'unit': unit,
                   'question': question,
                   'in_note_view': True}
                  )


@login_required
def create_question(request, source_pk, unit_pk):
    """
    Create a standalone Question note
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.unit = unit
            question.save()
            messages.success(request, "Question note saved.")
            return redirect('question-detail', source_pk, unit_pk, question.pk)
    else:
        form = QuestionForm()

    return render(request, 'notes/create_question.html', {
        'source': source,
        'unit': unit,
        'form': form,
        'in_note_view': True
    })


# --- MyWords Notes ---
@login_required
def mywords_detail(request, source_pk, unit_pk, mywords_pk):
    """Retrieve and display a single My Words note"""
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)
    mywords = get_object_or_404(MyWords, pk=mywords_pk, unit=unit)
    return render(request,
                  'notes/mywords_detail.html',
                  {'source': source,
                   'unit': unit,
                   'mywords': mywords,
                   'in_note_view': True}
                  )


@login_required
def create_mywords(request, source_pk, unit_pk):
    """
    Create a standalone My Words note
    """
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    unit = get_object_or_404(Unit, pk=unit_pk, source=source)

    if request.method == 'POST':
        form = MyWordsForm(request.POST)
        if form.is_valid():
            mywords = form.save(commit=False)
            mywords.unit = unit
            mywords.save()
            messages.success(request, "My Words note saved.")
            return redirect('mywords-detail', source_pk, unit_pk, mywords.pk)
    else:
        form = MyWordsForm()

    return render(request, 'notes/create_mywords.html', {
        'source': source,
        'unit': unit,
        'form': form,
        'in_note_view': True,
    })
