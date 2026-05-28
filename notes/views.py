from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, render, redirect
from .models import Source
from .forms import SourceForm


# Create your views here.
# Prevent browser caching
# so back button forces a fresh server request after logout
@never_cache
@login_required
def dashboard(request):
    return render(request, 'notes/dashboard.html')


def home(request):
    return render(request, 'notes/index.html')


@login_required
def sources_list(request):
    sources = Source.objects.filter(user=request.user)
    return render(request, 'notes/sources.html', {'sources': sources})


@login_required
def source_detail(request, source_pk):
    """Retrieve and display a single source belonging to the current user."""

    source = get_object_or_404(Source, pk=source_pk, user=request.user)
    return render(request, "notes/source_detail.html", {"source": source})


@login_required
def create_source(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            source = form.save(commit=False)
            source.user = request.user
            source.save()
            return redirect('source-detail', source_pk=source.pk)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SourceForm()
    return render(request, "notes/create_source.html", {"form": form})
