## Preparatory Steps
- Create urls.py in your app folder
<pre>
# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
</pre>

- Wire it into the project urls.py
<pre>
# project/urls.py
from django.urls import path, include  # don't forget include

urlpatterns = [
    path('app_name/', include('app_name.urls')),
]
</pre>

**Key things to remember:**
- include() must be imported from django.urls
- The prefix in the project urls (notes/) is prepended to all app-level paths — so path('', ...) in the app becomes /notes/
- Every app gets its own urls.py — Django doesn't create it automatically like views.py or models.py

## writing the view

If the view needs to display a dynamic HTML page, it needs a context.
<pre>
def view_name(request):
    data = Model.objects.filter(field=value)
    context = {'key': data}
    return render(request, 'app/template.html', context)
</pre>

What is the context?

- A plain Python dictionary passed as the third argument to render()
-nThe keys become variable names available in the template
- The values are the data you want to display

Without context the template is static — same HTML every time.
With context the template is dynamic — renders differently based on the data passed in.


**Key things to remember:**

- The context dictionary can hold anything: querysets, strings, numbers, lists, booleans
- Keep context assembly in the view, not the template — templates should only display, not query
- Can be passed inline for simple views: return render(request, 'template.html', {'key': value})