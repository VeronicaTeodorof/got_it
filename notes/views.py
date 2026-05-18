from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'notes/dashboard.html')


def home(request):
    return render(request, 'notes/index.html')