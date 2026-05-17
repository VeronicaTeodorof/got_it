from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello, Home!")


@login_required
def dashboard(request):
    return render(request, 'notes/dashboard.html')


def base(request):
    return render(request, 'base.html')