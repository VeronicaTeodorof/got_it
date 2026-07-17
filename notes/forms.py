from django import forms
from .models import Source, Unit, Reference, MyWords, Question


class SourceForm(forms.ModelForm):
    """A form for creating and editing Source instances."""

    # __init__ allows extra data (not part of the form fields) to be passed in
    # and made available to clean() for validation
    # __init__ instantiates the child, but on its own it overrides the parent
    # I need to add to the parent,
    # therefore the parent will be called at the end
    def __init__(self, *args, **kwargs):
        # pop 'user' from kwargs before passing to parent
        # pop extracts the value and removes the key from kwargs
        # if not removed, super().__init__() would raise a TypeError
        # None is the fallback if 'user' is not passed
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        new_choices = []
        for choice in self.fields['source_type'].choices:
            if choice[0] == '':
                new_choices.append(('', 'type'))
            else:
                new_choices.append(choice)
        self.fields['source_type'].choices = new_choices

    class Meta:
        model = Source
        fields = ["source_name", "source_author", "source_type"]
        labels = {
            'source_name': 'Name',
            'source_author': 'Author',
            'source_type': 'Type'
        }
        widgets = {
            'source_name': forms.TextInput(attrs={'class': 'form-input',
                                                  'placeholder': 'name'}),
            'source_author': forms.TextInput(attrs={'class': 'form-input',
                                                    'placeholder': 'author'}),
            'source_type': forms.Select(attrs={'class': 'form-input',
                                               'placeholder': 'type'}),
        }

    def clean_source_author(self):
        """
        Ensures absent author is saved as NULL, not an empty string.

        This is important for consistent filtering on sources without an author
        using source_author__isnull=True.
        """
        # safely retrieves source_author from cleaned_data,
        # returns None if key is missing
        author = self.cleaned_data.get('source_author')
        # .strip() handles the edge case where user types only spaces
        # "   ".strip() → "" which is falsy, so None is returned instead
        return author.strip() if author and author.strip() else None

    def clean(self):
        """
        Ensures duplicate source names per user are rejected with an error
        at form validation level
        """
        cleaned_data = super().clean()
        source_name = cleaned_data.get('source_name')
        queryset = Source.objects.filter(user=self.user,
                                         source_name=source_name)
        # Excludes cases where user wants to edit the same name again,
        #  without this condition raises error
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError({
                'source_name': "You already have a source with this name."
            })
        return cleaned_data


class UnitForm(forms.ModelForm):
    """
    A form for creating and editing a unit instance
    """
    def __init__(self, *args, **kwargs):
        self.source = kwargs.pop('source', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Unit
        fields = ["unit_name"]
        labels = {
            'unit_name': 'Unit name'
        }
        widgets = {
            'unit_name': forms.TextInput(attrs={'class': 'form-input',
                                                'placeholder': 'name'})
        }

    def clean(self):
        """
        Ensures duplicate unit names per source are rejected with an error
        at form validation level
        """
        cleaned_data = super().clean()
        unit_name = cleaned_data.get('unit_name')
        queryset = Unit.objects.filter(source=self.source, unit_name=unit_name)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError({
                'unit_name': "You already have a unit with this name."
            })
        return cleaned_data


class ReferenceForm(forms.ModelForm):
    """
    A form for creating and editing reference notes
    """
    class Meta:
        model = Reference
        fields = ['title', 'content', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input',
                                            'placeholder': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-input',
                                             'placeholder': 'content',
                                             'rows': 5}),
            'location': forms.TextInput(attrs={'class': 'form-input',
                                               'placeholder': 'location',
                                               }),
        }


class QuestionForm(forms.ModelForm):
    """
    A form for creating and editing question notes
    """
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input',
                                            'placeholder': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-input',
                                             'placeholder': 'content',
                                             'rows': 10}),
        }


class MyWordsForm(forms.ModelForm):
    """
    A form for creating and editing My Words notes
    """
    class Meta:
        model = MyWords
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input',
                                            'placeholder': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-input',
                                             'placeholder': 'content',
                                             'rows': 10}),
        }
