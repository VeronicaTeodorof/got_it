from django.test import TestCase
from notes.models import SourceType, Source
from django.contrib.auth.models import User


class SourceTypeModelTest(TestCase):
    """Tests for the SourceType model"""
    def test_source_type_model_exists(self):
        self.assertTrue(SourceType)


class SourceModelTest(TestCase):
    """Tests for the Source model"""
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@test.com',
            password='testpass')
        self.source_type = SourceType.objects.create()
        self.source = Source.objects.create(
            user=self.user,
            source_type=self.source_type
        )

    def test_source_model_exists(self):
        self.assertTrue(Source)

    def test_source_has_user_field(self):
        self.assertTrue(hasattr(Source, 'user'))

    def test_source_deleted_when_user_deleted(self):
        self.user.delete()
        self.assertFalse(Source.objects.filter(pk=self.source.pk).exists())

    def test_source_has_source_type_field(self):
        self.assertTrue(hasattr(Source, 'source_type'))
