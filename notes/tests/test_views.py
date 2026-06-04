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


class DashboardViewTest(TestCase):
    """Tests for dashboard page"""
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
        self.form_data = {
            'source_name': 'Name',
            'source_author': 'Author',
            'source_type': 'book'
        }

    def test_authenticated_user_gets_200(self):
        """SP-AT-01: Authenticated user can access the dashboard page."""
        self.client.login(
            username='user', email='user@testing.com', password='test'
            )
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_is_redirected(self):
        """SP-AT-02: Unauthenticated user is redirected to the login page."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_sees_own_sources(self):
        """SP-AT-03: User's own sources appear in the context."""
        self.client.login(
            username='user', email='user@testing.com', password='test'
        )
        response = self.client.get(reverse('dashboard'))
        self.assertIn(self.source, response.context['sources'])

    def test_authenticated_user_cannot_see_another_user_sources(self):
        """SP-AT-04: Authenticated user cannot see another user's sources"""
        user2 = User.objects.create_user(
            username='user2', email='user2@testing.com', password="test"
        )
        self.client.force_login(user2)
        response = self.client.get(reverse('dashboard'))
        self.assertNotIn(self.source, response.context['sources'])

    def test_duplicate_source_name_raises_error(self):
        """
        Test duplicate name for same user returns 200
        and raises error
        """
        self.client.force_login(self.user)
        Source.objects.create(
            user=self.user, source_name="Test", source_type="book"
            )
        response = self.client.post(
            reverse('dashboard'),
            data={'source_name': "Test", 'source_type': "book"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'error', response.context['form']['name'].errors.as_text()
            )


class SourceDetailViewTest(TestCase):
    """Tests for source detail page"""

    def setUp(self):
        """Create test user and source"""
        self.user = User.objects.create_user(
            username='user', email="user@testing.com", password="test"
        )
        self.source = Source.objects.create(
            user=self.user,
            source_type=Source.SourceType.BOOK,
            source_name='Test Source',
            source_author='Test Author'
        )

    def test_unauthenticated_user_is_redirected(self):
        """SDP-AT-01: Unauthenticated user is redirected to the login page."""
        url = reverse('source-detail', args=[self.source.pk])
        response = self.client.get(url)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_authenticated_user_can_see_own_source(self):
        """SDP-AT-02: Page requested by authenticated user loads correctly,
        with the right template and right context"""
        self.client.login(username='user', password='test')
        response = self.client.get(
            reverse('source-detail', args=[self.source.pk])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/source_detail.html')
        self.assertEqual(response.context['source'], self.source)

    def test_nonexistent_source_returns_404(self):
        """SDP-AT-03: 404 is returned for inexistent source"""
        self.client.login(username='user', password='test')
        response = self.client.get(reverse('source-detail', args=[1234]))
        self.assertEqual(response.status_code, 404)

    def test_user_cannot_access_other_users_source(self):
        """SDP-AT-04: Authenticated user cannot see another user's
        source detail"""
        user2 = User.objects.create_user(
            username='user2', password='test'
        )
        self.client.force_login(user2)
        response = self.client.get(
            reverse('source-detail', args=[self.source.pk])
            )
        self.assertEqual(response.status_code, 404)


class CreateSourceViewTest(TestCase):
    """Tests for create source page"""
    def setUp(self):
        """Create test user"""
        self.user = User.objects.create_user(
            username='user', email="user@testing.com", password="test")
        self.form_data = {
            'source_name': 'Name',
            'source_author': 'Author',
            'source_type': 'book'
        }

    def test_valid_submission_creates_source(self):
        """Valid submission creates source
        and redirects to source detail page"""
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('dashboard'), data=self.form_data
            )
        source = Source.objects.get(source_name='Name')
        self.assertRedirects(
            response, reverse('source-detail', kwargs={'source_pk': source.pk})
            )

    def test_source_saved_with_correct_user(self):
        """Source is saved with the correct user"""
        self.client.force_login(self.user)
        self.client.post(reverse('create-source'), data=self.form_data)
        source = Source.objects.get(source_name='Name')
        self.assertEqual(self.user, source.user)
