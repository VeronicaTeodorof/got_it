from django.test import TestCase
from notes.models import Source
from django.contrib.auth.models import User
from django.db import IntegrityError


class SourceModelTest(TestCase):
    """Tests for the Source model"""
    def setUp(self):
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

    def test_str_returns_name_by_author(self):
        self.assertEqual(str(self.source), 'Test Source by Test Author')

    def test_str_without_author_returns_source(self):
        self.source_no_author = Source.objects.create(
            user=self.user,
            source_type=Source.SourceType.BOOK,
            source_name='Test Source with No Author',
            source_author=None
        )
        self.assertEqual(
            str(self.source_no_author), 'Test Source with No Author'
            )

    def test_invalid_source_type_raises_error(self):
        with self.assertRaises(IntegrityError):
            Source.objects.create(
                user=self.user,
                source_type='paper',
                source_name='Test Invalid Type',
            )

    def test_source_type_displays_correctly(self):
        self.assertEqual(self.source.get_source_type_display(), 'Book')
