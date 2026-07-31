from django.test import TestCase
from notes.forms import SourceForm, UnitForm
from notes.models import Source, Unit
from django.contrib.auth.models import User


class SourceFormTest(TestCase):
    """Test for the Source form"""
    def setUp(self):
        """Creates test user and source"""
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='Name',
            source_type='book'
        )

    def test_empty_source_author_saved_as_none(self):
        """ANF-01: Empty author field is saved as None, not empty string"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_author': '',
            'source_type': 'book'
        })
        self.assertTrue(form.is_valid())
        self.assertIsNone(form.cleaned_data.get('source_author'))

    def test_white_spaces_only_for_author_saved_as_none(self):
        """ANF-02: Author field with spaces only is saved as None,
        not as name"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_author': '   ',
            'source_type': 'book'
        })
        self.assertTrue(form.is_valid())
        self.assertIsNone(form.cleaned_data.get('source_author'))

    def test_author_field_value_is_returned_correctly(self):
        """ANF-03: Author field with valid data is returned correctly"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_author': 'Author',
            'source_type': 'book'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('source_author'), 'Author')

    def test_duplicate_source_name_same_user_raises_error(self):
        """ANF-04: Same user creating a duplicate name source raises error"""
        form = SourceForm(data={
            'source_name': 'Name',
            'source_type': 'book'},
            user=self.user
        )
        self.assertFalse(form.is_valid())
        self.assertIn('source_name', form.errors)

    def test_other_user_same_source_name_submits_without_error(self):
        """ ANF-05: Source name uniqueness is enforced per user,
        not globally"""
        user = User.objects.create_user(
            username='different_user',
            password='secret'
        )
        form = SourceForm(data={
            'source_name': 'Name',
            'source_type': 'book'},
            user=user)
        self.assertTrue(form.is_valid())

    def test_editing_source_with_same_name_submits_correctly(self):
        """
        ANF-06: Editing a source with unchanged name doesn't raise error
        """
        form = SourceForm(data={
                    'source_name': 'Name',
                    'source_type': 'book'},
                    user=self.user,
                    instance=self.source
                )
        self.assertTrue(form.is_valid())


class UnitFormTest(TestCase):
    """
    Tests for the Unit form
    """
    def setUp(self):
        """
        Creates test user, source and unit
        """
        self.user = User.objects.create_user(username='tester',
                                             password='test')
        self.source = Source.objects.create(
            user=self.user,
            source_name='Source Name',
            source_type='book'
        )
        self.unit = Unit.objects.create(source=self.source,
                                        unit_name='Unit 1')

    def test_duplicate_unit_name_same_source_raises_error(self):
        """ANF-07: Creating a duplicate name unit within the same source
        raises error"""
        form = UnitForm(data={'unit_name': 'Unit 1'}, source=self.source)
        self.assertFalse(form.is_valid())
        self.assertIn('unit_name', form.errors)

    def test_same_unit_name_different_source_is_valid(self):
        """ANF-08: Unit name uniqueness is enforced per source, not globally"""
        other_source = Source.objects.create(
            user=self.user,
            source_name='Other Name',
            source_type='course'
        )
        form = UnitForm(data={'unit_name': 'Unit 1'}, source=other_source)
        self.assertTrue(form.is_valid())

    def test_editing_unit_with_unchanged_name_is_valid(self):
        """ANF-09: Editing a unit with its own unchanged name is valid"""
        form = UnitForm(data={'unit_name': 'Unit 1'},
                        source=self.source,
                        instance=self.unit)
        self.assertTrue(form.is_valid())
