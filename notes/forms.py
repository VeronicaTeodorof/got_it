from django import forms
from .models import Source


class SourceForm(forms.ModelForm):
    """A form for creating and editing Source instances."""
    class Meta:
        model = Source
        fields = ["source_name", "source_author", "source_type"]
        labels = {
            'source_name': 'Name',
            'source_author': 'Author',
            'source_type': 'Type'
        }

    def clean_source_author(self):
        """Ensures absent author is saved as NULL, not an empty string.

        This is important for consistent filtering on sources without an author
        using source_author__isnull=True.
        """
        # safely retrieves source_author from cleaned_data,
        # returns None if key is missing
        author = self.cleaned_data.get('source_author')
        # .strip() handles the edge case where user types only spaces
        # "   ".strip() → "" which is falsy, so None is returned instead
        return author.strip() if author and author.strip() else None
