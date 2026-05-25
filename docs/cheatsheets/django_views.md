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


## Detail views

A detail view retrieves a single object by its pk (primary key), which is captured from the URL.


**Key things to remember:**

- Use get_object_or_404() instead of Model.objects.get() — it handles the missing object case automatically by returning a 404 page instead of crashing
- Always filter by user as well as pk — otherwise a logged-in user could access another user's data by guessing the URL
- Use @login_required on any view that displays user data — it redirects unauthenticated users to the login page
- The URL parameter name (source_pk) must match the view function parameter name exactly
- For nested URLs (e.g. /sources/4/units/3/), name parameters distinctly (source_pk, unit_pk) and validate the hierarchy: get_object_or_404(Unit, pk=unit_pk, source_id=source_pk)
- The context key is arbitrary — {'source': ...} makes it available as {{ source }} in the template, but any name works