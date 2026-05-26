from django.test import TestCase
from notes.forms import SourceForm


class SourceFormTest(TestCase):
    """Test for the Source form"""

    def test_empty_source_author_saved_as_none(self):
        """Empty author field is saved as None, not empty string"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_author': '',
            'source_type': 'book'
        })
        form.is_valid()
        self.assertIsNone(form.cleaned_data.get('source_author'))

    def test_white_spaces_only_for_author_saved_as_none(self):
        """Author field with spaces only is saved as None, not as name"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_author': '   ',
            'source_type': 'book'
        })
        form.is_valid()
        self.assertIsNone(form.cleaned_data.get('source_author'))

    def test_author_field_value_is_returned_correctly(self):
        """Author field with valid data is returned correctly"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_author': 'Author',
            'source_type': 'book'
        })
        form.is_valid()
        self.assertEqual(form.cleaned_data.get('source_author'), 'Author')
