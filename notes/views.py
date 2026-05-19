from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import render


# Create your views here.
# Prevent browser caching
# so back button forces a fresh server request after logout
@never_cache
@login_required
def dashboard(request):
    return render(request, 'notes/dashboard.html')


def home(request):
    return render(request, 'notes/index.html')
