from django.test import TestCase
from django.urls import reverse


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
    """Tests for the signin page."""

    def test_signin_page_loads(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_signin_page_contains_signin_link(self):
        response = self.client.get(reverse('account_login'))
        self.assertContains(
            response,
            f'then please <a href="{reverse("account_signup")}">'
        )
