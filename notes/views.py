from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect
from .models import Source
from .forms import SourceForm
from django.http import JsonResponse


# Create your views here.
# Prevent browser caching
# so back button forces a fresh server request after logout
@never_cache
@login_required
def dashboard(request):
    """
    Retrieve and display a list of sources belonging to the current user.
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
    return render(
        request, 'notes/dashboard.html', {'form': form, 'sources': sources}
        )


def home(request):
    return render(request, 'notes/index.html')


@login_required
def source_detail(request, source_pk):
    """Retrieve and display a single source belonging to the current user."""

    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    return render(request, "notes/source_detail.html", {"source": source})


@login_required
def edit_source(request, source_pk):
    """ View for the editSourceModal"""
    # Retrieve the specific record from the database using the pk
    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    if request.method == 'POST':
        # Bind the submitted data to the form in the POST block
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    # Instantiate the form with the fetched source
    form = SourceForm(instance=source)
    return render(
        request,
        'notes/edit_source_form.html',
        {'form': form, 'source': source}
        )


def delete_source(request, source_pk):
    """View for deleteSourceModal
    """
    if request.method == 'POST':
        source = get_object_or_404(Source, pk=source_pk, user=request.user)
        source.delete()
        return redirect('sources-list')
