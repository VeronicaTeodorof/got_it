# Django Forms


## Core concepts

- Field — defines what data is accepted and validated
- Widget — defines how a field is rendered in HTML (presentation only, doesn't affect validation)
- forms.py — convention for defining form classes, lives in the app directory, no database involvement
- ModelForm — generates form fields automatically from a model, use when creating/editing model instances
- Plain Form — use for forms not tied to a model (e.g. search, contact)


<pre>
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']  # only fields the user should fill in
        labels = {
            'field1': 'Custom Label'
        }
</pre>


- fields — only include what the user fills in; exclude auto-managed fields (timestamps, user, etc.)
- ModelForm auto-generates fields not explicitly defined in the class body
- Labels default to field name with underscores replaced by spaces and first letter capitalised


**Widgets**

- Default widgets are chosen automatically based on field type
- Override with widget= parameter
- Customise HTML attributes with attrs=

<pre>
title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
</pre>


**Validation**

- is_valid() must be called explicitly in the view
- On success, populates form.cleaned_data — a dictionary of validated, Python-typed values
- Always use cleaned_data over request.POST — raw POST data is always strings
- cleaned_data.get('field') — safe retrieval, returns None if key missing
- cleaned_data['field'] — raises KeyError if key missing

**Custom field cleaning**

Define clean_<fieldname>() on the form — Django calls it automatically during validation

<pre>
def clean_source_author(self):
    # safely retrieves source_author from cleaned_data,
    # returns None if key is missing
    author = self.cleaned_data.get('source_author')
    # .strip() handles the edge case where user types only spaces
    # "   ".strip() → "" which is falsy, so None is returned instead
    return author.strip() if author and author.strip() else None
</pre>

