from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from notes.models import Source, Unit, Reference


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
            'You already have a source with this name.',
            response.context['form']['source_name'].errors.as_text()
        )

    def test_source_saved_with_correct_user(self):
        """Source is saved with the correct user"""
        self.client.force_login(self.user)
        self.client.post(reverse('dashboard'), data=self.form_data)
        source = Source.objects.get(source_name='Name')
        self.assertEqual(self.user, source.user)

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

    def test_source_forms_is_passed_in_context(self):
        """Context includes source_forms"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('dashboard'))
        self.assertIn('source_forms', response.context)

    def test_prepopulated_data_in_edit_form_matches_source(self):
        """Correct data prepopulates the fields in an edit form"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('dashboard'))
        source_forms = response.context['source_forms']
        source, form = source_forms[0]
        self.assertEqual(self.source, source)
        self.assertEqual(form.instance, self.source)


class SourceDetailViewTest(TestCase):
    """Tests for source detail page"""

    def setUp(self):
        """Create test user, source and unit"""
        self.user = User.objects.create_user(
            username='user', email="user@testing.com", password="test"
        )
        self.source = Source.objects.create(
            user=self.user,
            source_type=Source.SourceType.BOOK,
            source_name='Test Source',
            source_author='Test Author'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='Unit 1'
        )
        self.unit2 = Unit.objects.create(
            source=self.source,
            unit_name='unit2'
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
        self.assertEqual(response.context['current_source'], self.source)

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

    def test_units_only_show_on_source_they_belong_to(self):
        """
        Tests that units are only displayed
        in the list of units belonging to their parent source
        """
        self.client.force_login(self.user)
        source2 = Source.objects.create(
            user=self.user,
            source_name='source2',
            source_type='book'
        )
        pk = source2.pk
        response = self.client.get(
            reverse('source-detail', args=[pk])
        )
        self.assertNotIn(self.unit, response.context['units'])

    def test_all_units_in_source_fetched_in_list(self):
        """Tests that all units belonging to a source
        are filtered in the queryset
        """
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('source-detail', args=[self.source.pk])
            )
        self.assertEqual(len(response.context['units']), 2)

    def test_form_with_blank_unit_name_rerenders_page_with_errors(self):
        """
        When a form is submitted blank, page reloads with form errors
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('source-detail',
                    args=[self.source.pk]),
            data={'unit_name': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertContains(response, 'This field is required.')
        self.assertTemplateUsed(response, 'notes/source_detail.html')

    def test_duplicate_unit_name_raises_error(self):
        """
        SDP-AT-07: Test duplicate unit name for same source returns 200
        and raises error
        """
        self.client.force_login(self.user)
        Unit.objects.create(
            source=self.source, unit_name='Unit1'
            )
        response = self.client.post(
            reverse('source-detail', args=[self.source.pk]),
            data={'unit_name': "Unit1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'You already have a unit with this name.',
            response.context['form']['unit_name'].errors.as_text()
        )


class EditSourceViewTest(TestCase):
    """
    Tests for the edit_source view.
    """
    def setUp(self):
        """Creates temporary user, source and form"""
        self.user = User.objects.create_user(
            email='something.com', password='test',  username='tester',
            )
        self.user2 = User.objects.create_user(
            username='tester2', password='example'
            )
        self.source = Source.objects.create(
            user=self.user,
            source_name='name',
            source_type='book'
        )
        self.form_data = {
            'source_name': 'Name2',
            'source_author': 'Author',
            'source_type': 'book'
        }

    def test_authenticated_owner_gets_200(self):
        """Authenticated user requesting to edit their
        source gets a 200 status code.
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'edit_source', args=[self.source.pk]
            ))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_gets_404_for_another_user_source(self):
        """Authenticated user trying to edit a source
        that does not belong to them gets 404.
        """
        self.client.force_login(self.user2)
        response = self.client.get(reverse(
            'edit_source', args=[self.source.pk]
            ))
        self.assertEqual(response.status_code, 404)

    def test_authenticated_user_gets_404_for_missing_source(self):
        """
        Authenticated user trying to edit a source that is missing
        gets 404.
        """
        self.client.force_login(self.user)
        pk = self.source.pk
        self.source.delete()
        response = self.client.get(reverse(
            'edit_source', args=[pk]
            ))
        self.assertEqual(response.status_code, 404)

    def test_valid_edit_submission_redirects_to_dashboard(self):
        """
        User is redirected to dashboard
        after successfully editing their source
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('edit_source', args=[self.source.pk]), data=self.form_data
            )
        self.assertEqual(response.status_code, 302)

    def test_form_is_passed_in_context(self):
        """Context includes form"""
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'edit_source', args=[self.source.pk]
            ))
        self.assertIn('form', response.context)

    def test_correct_template_is_used(self):
        """
        Correct template is given in response
        """
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('edit_source', args=[self.source.pk]
                    ))
        self.assertTemplateUsed(response, 'notes/dashboard.html')


class DeleteSourceView(TestCase):
    """
    Tests for delete source view
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email='something.com', password='test',  username='tester',
            )
        self.source = Source.objects.create(
            user=self.user,
            source_name='name',
            source_type='book'
        )
        self.source2 = Source.objects.create(
            user=self.user,
            source_name='other name',
            source_type='website'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='unit'
        )

    def test_right_source_is_deleted_and_no_other_source_is(self):
        self.client.force_login(self.user)
        sources = Source.objects.all()
        self.client.post(
            reverse('delete_source', args=[self.source.pk]))
        self.assertNotIn(self.source, sources)
        self.assertEqual(1, len(sources))

    def test_authenticated_user_gets_404_for_missing_source(self):
        """
        Authenticated user trying to delete a source that doesn't exist
        gets 404.
        """
        self.client.force_login(self.user)
        self.source.delete()
        response = self.client.get('/sources/800/delete/')
        self.assertEqual(response.status_code, 404)

    def test_unauthenticated_user_visits_source_delete_url_redirects(self):
        """
        Unauthenticated user requests delete url of an existing source and
        gets redirected to login page
        """
        response = self.client.get(reverse(
            'delete_source', args=[self.source.pk]
            ))
        self.assertEqual(response.status_code, 302)


class UnitDetailView(TestCase):
    """
    Tests for unit detail view
    """

    def setUp(self):
        """
        Creates user, source and unit
        """
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='source',
            source_type='book'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='unit'
        )

    def test_authenticated_owner_accessing_unit_detail_page_gets_200(self):
        """
        Authenticated owner gets 200 status code when requesting
            detail page of a unit
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'unit-detail',
            args=[self.source.pk, self.unit.pk]
            ))
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_redirected(self):
        """
        Any unauthenticated user is redirected
        when trying to access a unit detail page
        """
        response = self.client.get(reverse(
            'unit-detail',
            args=[self.source.pk, self.unit.pk]
        ))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_gets_404_for_another_user_unit(self):
        """
        Authenticated user trying to access another user's unit detail page
        gets 404 response
        """
        user2 = User.objects.create_user(
            username='tester2',
            password='test'
        )
        self.client.force_login(user2)
        response = self.client.get(reverse(
            'unit-detail',
            args=[self.source.pk, self.unit.pk]
            ))
        self.assertEqual(response.status_code, 404)

    def test_authenticated_user_gets_404_for_inexistent_unit(self):
        """
        Authenticated user requesting a unit that doesn't exists gets 404
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'unit-detail',
            args=[self.source.pk, 800]
        ))
        self.assertEqual(response.status_code, 404)

    def test_unit_name_is_correctly_displayed(self):
        """
        Unit name correctly shows on unit detail page
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'unit-detail',
            args=[self.source.pk, self.unit.pk]
        ))
        self.assertContains(response, self.unit.unit_name)

    def test_successful_unit_creation_redirects_to_unit_page(self):
        """
        User is redirected to unit detail page
        after successfully creating a unit.
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('source-detail',
                    args=[self.source.pk]
                    ),
            data={'unit_name': 'Unit1'}
        )
        self.assertEqual(response.status_code, 302)
        unit = Unit.objects.get(unit_name='Unit1')
        self.assertRedirects(response,
                             reverse('unit-detail',
                                     kwargs={'source_pk': self.source.pk,
                                             'unit_pk': unit.pk}))


class EditUnitView(TestCase):
    """
    Tests for the edit unit view
    """
    def setUp(self):
        """
        Creates user, source, unit and unit form
        """
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='name',
            source_type='book'

        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='unit'
        )

    def test_get_request_for_edit_unit(self):
        """Test if get request for edit unit form gives 200 status code,
        the right template, and the right context.
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'edit-unit', args=[self.source.pk, self.unit.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/source_detail.html')
        self.assertIn('form', response.context)
        # asserts that the form is prepopulated with correct data
        self.assertEqual(response.context['form'].instance, self.unit)


class ReferenceDetailVeiw(TestCase):
    """
    Tests for reference detail view
    """
    def setUp(self):
        """
        Creates user, source, unit and reference note
        """
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='name',
            source_type='book'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='name',
        )
        self.reference = Reference.objects.create(
            unit=self.unit,
            content='content'
        )

    def test_authenticated_owner_gets_200(self):
        """
        Authenticated owner can access reference note
        """
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('reference-detail',
                    args=[self.source.pk, self.unit.pk, self.reference.pk]))
        self.assertEqual = (response.status_code, 200)
