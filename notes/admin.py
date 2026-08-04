from django.contrib import admin
from .models import Source, Unit, Reference, MyWords, Question

# Register your models here.
admin.site.register(Source)
admin.site.register(Unit)
admin.site.register(Reference)
admin.site.register(MyWords)
admin.site.register(Question)
