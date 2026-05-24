from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from notes.models import Source


class HomeViewTest(TestCase):
    """Tests for the home page."""

    def test_home_page_loads(self):
        # self.client is a test browser provided by Django's TestCase
        # self.client.get() simulates a GET request to a URL
        # reverse() converts a URL name into its actual URL path
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class SignUpViewTest(TestCase):
    """Tests for the signup page."""

    def test_signup_page_loads(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_contains_signin_link(self):
        response = self.client.get(reverse('account_signup'))
        self.assertContains(
            response,
            f'Already have an account? <a href="{reverse("account_login")}">'
        )


class SignInViewTest(TestCase):
    """Tests for the signin page"""

    def test_signin_page_loads(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_signin_page_contains_signin_link(self):
        response = self.client.get(reverse('account_login'))
        self.assertContains(
            response,
            f'then please <a href="{reverse("account_signup")}">'
        )


class SourcesListViewTest(TestCase):
    """Tests for sources page"""
    def setUp(self):
        """Create test user and source"""
        self.user = User.objects.create_user(
            username='user', email='user@testing.com', password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_type=Source.SourceType.BOOK,
            source_name='Test Source',
            source_author='Test Author'
        )

    def test_authenticated_user_gets_200(self):
        """SP-AT-01: Authenticated user can access the sources page."""
        self.client.login(
            username='user', email='user@testing.com', password='test'
            )
        response = self.client.get(reverse('sources-list'))
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_is_redirected(self):
        """SP-AT-02: Unauthenticated user is redirected to the login page."""
        response = self.client.get(reverse('sources-list'))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_sees_own_sources(self):
        """SP-AT-03: User's own sources appear in the context."""
        self.client.login(
            username='user', email='user@testing.com', password='test'
        )
        response = self.client.get(reverse('sources-list'))
        self.assertIn(self.source, response.context['sources'])

    def test_authenticated_user_cannot_see_another_user_sources(self):
        """SP-AT-04: Authenticated user cannot see another user's sources"""
        user2 = User.objects.create_user(
            username='user2', email='user2@testing.com', password="test"
        )
        self.client.force_login(user2)
        response = self.client.get(reverse('sources-list'))
        self.assertNotIn(self.source, response.context['sources'])
