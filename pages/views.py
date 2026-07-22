from django.shortcuts import render

# Create your views here.


# --- Home ---
def home(request):
    return render(request, 'pages/index.html')

# --- How it works ---
def help(request):
    return render(request, 'pages/how_it_works.html')
