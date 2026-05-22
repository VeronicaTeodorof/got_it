from django.test import TestCase
from notes.models import SourceType, Source
from django.contrib.auth.models import User


class SourceModelTest(TestCase):
    """Tests for the Source model"""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass')
        self.source_type = SourceType.objects.create()
        self.source = Source.objects.create(
            user=self.user,
            source_type=self.source_type
        )

    def test_source_deleted_when_user_deleted(self):
        self.user.delete()
        self.assertFalse(Source.objects.filter(pk=self.source.pk).exists())


