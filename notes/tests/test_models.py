from django.test import TestCase
from notes.models import Source, Unit
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ValidationError


class SourceModelTest(TestCase):
    """ Tests for the Source model"""
    def setUp(self):
        """
        Creates test user and source for the entire class
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass')
        self.source = Source.objects.create(
            user=self.user,
            source_type=Source.SourceType.BOOK,
            source_name='Test Source',
            source_author='Test Author'
        )

    def test_duplicate_source_name_per_user_raises_error(self):
        """ANM-01: Tests that user trying to save duplicate name source
        gets error"""
        with self.assertRaises(IntegrityError):
            Source.objects.create(
                user=self.user,
                source_type=Source.SourceType.BOOK,
                source_name='Test Source')

    def test_duplicate_source_name_enforced_per_user_not_globaly(self):
        """ANM-02: Tests that two different users can have sources with same name,
        one per user, duplicate constraint enforced per user, not globally
        """
        user = User.objects.create_user(
            username='tester',
            email='testing@test.com',
            password='testpass')
        other_source = Source.objects.create(
            user=user,
            source_type=Source.SourceType.BOOK,
            source_name='Test Source'
        )
        self.assertEqual(other_source.source_name, 'Test Source')
        self.assertNotEqual(user, self.user)

    def test_valid_source_type_saves_without_errors(self):
        """
        ANM-03: Tests that valid source type saves without problems
        """
        other_source = Source.objects.create(
            user=self.user,
            source_type=Source.SourceType.BOOK,
            source_name='Some Source'
        )
        self.assertEqual(other_source.source_type, Source.SourceType.BOOK)

    def test_invalid_source_type_raises_error(self):
        """
        ANM-04: Tests that trying to save a source with invalid source type raises
        error
        """
        with self.assertRaises(IntegrityError):
            Source.objects.create(
                user=self.user,
                source_type='invalid',
                source_name='Some Source'
            )

#     def test_str_returns_name_by_author(self):
#         self.assertEqual(str(self.source), 'Test Source by Test Author')

#     def test_str_without_author_returns_source(self):
#         self.source_no_author = Source.objects.create(
#             user=self.user,
#             source_type=Source.SourceType.BOOK,
#             source_name='Test Source with No Author',
#             source_author=None
#         )
#         self.assertEqual(
#             str(self.source_no_author), 'Test Source with No Author'
#             )

#     def test_invalid_source_type_raises_error(self):
#         with self.assertRaises(IntegrityError):
#             Source.objects.create(
#                 user=self.user,
#                 source_type='paper',
#                 source_name='Test Invalid Type',
#             )

#     def test_source_type_displays_correctly(self):
#         self.assertEqual(self.source.get_source_type_display(), 'Book')


# class UnitModelTest(TestCase):
#     """Tests for Unit Model"""

#     def setUp(self):
#         """
#         Creates user, source and unit instances for the unit model tests
#         """
#         self.user = User.objects.create_user(
#             username='tester',
#             password='test'
#         )
#         self.source = Source.objects.create(
#             user=self.user,
#             source_name='test_source',
#             source_author='author',
#             source_type='book'
#         )
#         self.unit = Unit.objects.create(
#             source=self.source,
#             unit_name='test_unit'
#         )

#         def test_duplicate_unit_name_raises_error(self):
#             """
#             Creating a new unit with a duplicate name raises error
#             """
#             unit2 = Unit(source=self.source, unit_name='test_unit')
#             with self.assertRaises(ValidationError):
#                 unit2.full_clean()
