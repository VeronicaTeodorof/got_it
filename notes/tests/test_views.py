from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from notes.models import Source, Unit


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
        """ANV-06: Authenticated user can access the dashboard page."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('notes:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_is_redirected(self):
        """ANV-05: Unauthenticated user is redirected to the login page."""
        response = self.client.get(reverse('notes:dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_sees_own_sources(self):
        """ANV-01: User's own sources appear in the context."""
        self.client.login(
            username='user', email='user@testing.com', password='test'
        )
        response = self.client.get(reverse('notes:dashboard'))
        self.assertIn(self.source, response.context['sources'])

    def test_authenticated_user_cannot_see_another_user_sources(self):
        """ANV-02: Authenticated user cannot see another user's sources"""
        user2 = User.objects.create_user(
            username='user2', email='user2@testing.com', password="test"
        )
        self.client.force_login(user2)
        response = self.client.get(reverse('notes:dashboard'))
        self.assertNotIn(self.source, response.context['sources'])

    def test_source_saved_with_correct_user(self):
        """ANV-03: Source is saved with the correct user"""
        self.client.force_login(self.user)
        self.client.post(reverse('notes:dashboard'), data=self.form_data)
        source = Source.objects.get(source_name='Name')
        self.assertEqual(self.user, source.user)

    def test_valid_submission_creates_source(self):
        """ANV-04: Valid submission creates source
        and redirects to source detail page"""
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('notes:dashboard'), data=self.form_data
            )
        Source.objects.get(source_name='Name')
        self.assertRedirects(
            response, reverse('notes:dashboard')
            )

    def test_invalid_submission_rerenders_dashboard(self):
        """ANV-07: Invalid submission re-renders dashboard
        instead of redirecting"""
        self.client.force_login(self.user)
        response = self.client.post(reverse('notes:dashboard'), {
            'source_name': '',
            'source_type': 'book',
        })
        self.assertEqual(response.status_code, 200)


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

    def test_units_only_show_on_source_they_belong_to(self):
        """
        ANV-12: Tests that units are only displayed
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
            reverse('notes:source-detail', args=[pk])
        )
        self.assertNotIn(self.unit, response.context['units'])

    def test_all_units_in_source_fetched_in_list(self):
        """ANV-11: Tests that all units belonging to a source
        are filtered in the queryset
        """
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('notes:source-detail', args=[self.source.pk])
            )
        self.assertIn(self.unit, response.context['units'])
        self.assertIn(self.unit2, response.context['units'])
        self.assertEqual(len(response.context['units']), 2)

    def test_edit_mode_false_by_default(self):
        """
        ANV-13: Tests that source details are not editable by default
        """
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('notes:source-detail', args=[self.source.pk])
        )
        self.assertFalse(response.context['edit_mode'])

    def test_valid_edit_source_submission_saves_and_redirects(self):
        """
        Valid edit_source submission updates the source and redirects
        to source detail page.
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('notes:source-detail', args=[self.source.pk]),
            data={
                'form_type': 'edit_source',
                'source_name': 'Updated Name',
                'source_author': 'Updated Author',
                'source_type': 'book',
            }
        )
        self.source.refresh_from_db()
        self.assertEqual(self.source.source_name, 'Updated Name')
        self.assertEqual(self.source.source_author, 'Updated Author')
        self.assertRedirects(
            response, reverse('notes:source-detail', args=[self.source.pk])
        )

    def test_edit_mode_true_on_invalid_edit_source_submission(self):
        """
        ANV-15: Tests that invalid submission triggers page
        rerender in edit mode
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('notes:source-detail',
                    args=[self.source.pk]),
            data={'form_type': 'edit_source',
                  'source_name': '',
                  'source_type': 'book'}
        )
        self.assertTrue(response.context['edit_mode'])

    def test_valid_add_unit_submission_creates_unit_and_redirects(self):
        """
        ANV-16: Valid add_unit submission creates a unit linked to the source
        and redirects to source detail page.
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('notes:source-detail', args=[self.source.pk]),
            data={
                'form_type': 'add_unit',
                'unit_name': 'New Unit',
            }
        )
        unit = Unit.objects.get(unit_name='New Unit')
        self.assertEqual(unit.source, self.source)
        self.assertRedirects(
            response, reverse('notes:source-detail', args=[self.source.pk])
        )

    def test_invalid_add_unit_submission_does_not_create_unit(self):
        """
        Invalid add_unit submission re-renders the page and does not
        create a unit.
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('notes:source-detail', args=[self.source.pk]),
            data={
                'form_type': 'add_unit',
                'unit_name': '',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Unit.objects.filter(unit_name='').exists())


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
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='unit'
        )

    def test_authenticated_user_gets_404_for_missing_source(self):
        """
        ANV-09: Authenticated user trying to delete a source that doesn't exist
        gets 404.
        """
        self.client.force_login(self.user)
        self.source.delete()
        response = self.client.get('/notes/sources/800/delete/')
        self.assertEqual(response.status_code, 404)

    def test_unauthenticated_user_visits_source_delete_url_redirects(self):
        """
        ANV-08: Unauthenticated user requests delete url of an existing source
        and gets redirected to login page
        """
        response = self.client.get(reverse(
            'notes:delete-source', args=[self.source.pk]
            ))
        self.assertEqual(response.status_code, 302)

    def test_owner_can_delete_own_source(self):
        """
        ANV-10: Authenticated user can delete their source
        and is redirected to dashboard
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('notes:delete-source', args=[self.source.pk])
        )
        self.assertRedirects(response, reverse('notes:dashboard'))
        self.assertFalse(Source.objects.filter(pk=self.source.pk).exists())


# class UnitDetailView(TestCase):
#     """
#     Tests for unit detail view
#     """

#     def setUp(self):
#         """
#         Creates user, source and unit
#         """
#         self.user = User.objects.create_user(
#             username='tester',
#             password='test'
#         )
#         self.source = Source.objects.create(
#             user=self.user,
#             source_name='source',
#             source_type='book'
#         )
#         self.unit = Unit.objects.create(
#             source=self.source,
#             unit_name='unit'
#         )

#     def test_authenticated_owner_accessing_unit_detail_page_gets_200(self):
#         """
#         Authenticated owner gets 200 status code when requesting
#             detail page of a unit
#         """
#         self.client.force_login(self.user)
#         response = self.client.get(reverse(
#             'unit-detail',
#             args=[self.source.pk, self.unit.pk]
#             ))
#         self.assertEqual(response.status_code, 200)

#     def test_unauthenticated_user_redirected(self):
#         """
#         Any unauthenticated user is redirected
#         when trying to access a unit detail page
#         """
#         response = self.client.get(reverse(
#             'unit-detail',
#             args=[self.source.pk, self.unit.pk]
#         ))
#         self.assertEqual(response.status_code, 302)

#     def test_authenticated_user_gets_404_for_another_user_unit(self):
#         """
#         Authenticated user trying to access another user's unit detail page
#         gets 404 response
#         """
#         user2 = User.objects.create_user(
#             username='tester2',
#             password='test'
#         )
#         self.client.force_login(user2)
#         response = self.client.get(reverse(
#             'unit-detail',
#             args=[self.source.pk, self.unit.pk]
#             ))
#         self.assertEqual(response.status_code, 404)

#     def test_authenticated_user_gets_404_for_inexistent_unit(self):
#         """
#         Authenticated user requesting a unit that doesn't exists gets 404
#         """
#         self.client.force_login(self.user)
#         response = self.client.get(reverse(
#             'unit-detail',
#             args=[self.source.pk, 800]
#         ))
#         self.assertEqual(response.status_code, 404)

#     def test_unit_name_is_correctly_displayed(self):
#         """
#         Unit name correctly shows on unit detail page
#         """
#         self.client.force_login(self.user)
#         response = self.client.get(reverse(
#             'unit-detail',
#             args=[self.source.pk, self.unit.pk]
#         ))
#         self.assertContains(response, self.unit.unit_name)

#     def test_successful_unit_creation_redirects_to_unit_page(self):
#         """
#         User is redirected to unit detail page
#         after successfully creating a unit.
#         """
#         self.client.force_login(self.user)
#         response = self.client.post(
#             reverse('source-detail',
#                     args=[self.source.pk]
#                     ),
#             data={'unit_name': 'Unit1'}
#         )
#         self.assertEqual(response.status_code, 302)
#         unit = Unit.objects.get(unit_name='Unit1')
#         self.assertRedirects(response,
#                              reverse('unit-detail',
#                                      kwargs={'source_pk': self.source.pk,
#                                              'unit_pk': unit.pk}))


# class EditUnitView(TestCase):
#     """
#     Tests for the edit unit view
#     """
#     def setUp(self):
#         """
#         Creates user, source, unit and unit form
#         """
#         self.user = User.objects.create_user(
#             username='tester',
#             password='test'
#         )
#         self.source = Source.objects.create(
#             user=self.user,
#             source_name='name',
#             source_type='book'

#         )
#         self.unit = Unit.objects.create(
#             source=self.source,
#             unit_name='unit'
#         )

#     def test_get_request_for_edit_unit(self):
#         """Test if get request for edit unit form gives 200 status code,
#         the right template, and the right context.
#         """
#         self.client.force_login(self.user)
#         response = self.client.get(reverse(
#             'edit-unit', args=[self.source.pk, self.unit.pk]
#         ))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'notes/source_detail.html')
#         self.assertIn('form', response.context)
#         # asserts that the form is prepopulated with correct data
#         self.assertEqual(response.context['form'].instance, self.unit)


# class ReferenceDetailVeiw(TestCase):
#     """
#     Tests for reference detail view
#     """
#     def setUp(self):
#         """
#         Creates user, source, unit and reference note
#         """
#         self.user = User.objects.create_user(
#             username='tester',
#             password='test'
#         )
#         self.source = Source.objects.create(
#             user=self.user,
#             source_name='name',
#             source_type='book'
#         )
#         self.unit = Unit.objects.create(
#             source=self.source,
#             unit_name='name',
#         )
#         self.reference = Reference.objects.create(
#             unit=self.unit,
#             content='content'
#         )

#     def test_authenticated_owner_gets_200(self):
#         """
#         Authenticated owner can access reference note
#         """
#         self.client.force_login(self.user)
#         response = self.client.get(
#             reverse('reference-detail',
#                     args=[self.source.pk, self.unit.pk, self.reference.pk]))
#         self.assertEqual = (response.status_code, 200)
