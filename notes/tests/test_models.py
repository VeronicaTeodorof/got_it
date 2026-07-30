from django.test import TestCase
from notes.models import Source, Unit, Reference, Question, MyWords
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
        """ANM-02: Tests that two different users can have sources
        with same name,one per user, duplicate constraint enforced per user,
        not globally
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
        ANM-04: Tests that trying to save a source with invalid source type
        raises error
        """
        with self.assertRaises(IntegrityError):
            Source.objects.create(
                user=self.user,
                source_type='invalid',
                source_name='Some Source'
            )


class UnitModelTest(TestCase):
    """Tests for Unit Model"""

    def setUp(self):
        """
        Creates user, source and unit instances for the unit model tests
        """
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='test_source',
            source_author='author',
            source_type='book'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='test_unit'
        )

    def test_duplicate_unit_name_raises_error(self):
        """
        ANM-05: Creating a new unit with a duplicate name raises error
        """
        unit2 = Unit(source=self.source, unit_name='test_unit')
        with self.assertRaises(ValidationError):
            unit2.full_clean()

    def test_same_unit_name_in_different_sources_saves(self):
        """
        ANM-06: Test two distinct sources can have units with same name
        """
        other_source = Source.objects.create(
            user=self.user,
            source_name='test1_source',
            source_author='author',
            source_type='book'
        )
        other_unit = Unit.objects.create(
                    source=other_source,
                    unit_name='test_unit'
        )
        self.assertEqual(other_unit.unit_name, self.unit.unit_name)
        self.assertNotEqual(other_unit.source, self.unit.source)


class QuestionModelTest(TestCase):
    """Tests for Question Model"""

    def setUp(self):
        """
        Creates user, source, unit and reference instances
        for the question model tests
        """
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='test_source',
            source_author='author',
            source_type='book'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='test_unit'
        )
        self.reference = Reference.objects.create(
            unit=self.unit,
            content='some content'
        )

    def test_deleting_reference_does_not_delete_linked_questions(self):
        """
        ANM-07: Tests that deleting the reference note set as foreign key on a
        question note does not delete the question as well
        """
        question = Question.objects.create(
            unit=self.unit,
            reference=self.reference,
            content='question content'
        )
        self.reference.delete()
        self.assertTrue(Question.objects.filter(pk=question.pk).exists())

    def test_deleting_reference_sets_question_reference_to_null(self):
        """
        ANM-08: Tests that deleting a reference note sets reference field to
        null on linked questions
        """
        question = Question.objects.create(
            unit=self.unit,
            reference=self.reference,
            content='question content'
        )
        self.reference.delete()
        question.refresh_from_db()
        self.assertIsNone(question.reference)


class MyWordsModelTest(TestCase):
    """Tests for MyWords Model"""

    def setUp(self):
        """
        Creates user, source, unit, reference and question instances
        for the mywords model tests
        """
        self.user = User.objects.create_user(
            username='tester',
            password='test'
        )
        self.source = Source.objects.create(
            user=self.user,
            source_name='test_source',
            source_author='author',
            source_type='book'
        )
        self.unit = Unit.objects.create(
            source=self.source,
            unit_name='test_unit'
        )
        self.reference = Reference.objects.create(
            unit=self.unit,
            content='some content'
        )
        self.question = Question.objects.create(
            unit=self.unit,
            reference=self.reference,
            content='question content'
        )

    def test_deleting_reference_does_not_delete_linked_mywords(self):
        """
        ANM-09: Tests that deleting the reference note set as foreign key on a
        mywords note does not delete mywords note as well
        """
        mywords = MyWords.objects.create(
            unit=self.unit,
            reference=self.reference,
            content='mywords content'
        )
        self.reference.delete()
        self.assertTrue(MyWords.objects.filter(pk=mywords.pk).exists())

    def test_deleting_reference_sets_mywords_reference_to_null(self):
        """
        ANM-10: Tests that deleting a reference note sets reference field to
        null on linked my words note
        """
        mywords = MyWords.objects.create(
            unit=self.unit,
            reference=self.reference,
            content='my words content'
        )
        self.reference.delete()
        mywords.refresh_from_db()
        self.assertIsNone(mywords.reference)

    def test_deleting_question_does_not_delete_linked_mywords(self):
        """
        ANM-11: Tests that deleting the question note set as foreign key on a
        mywords note does not delete mywords note as well
        """
        mywords = MyWords.objects.create(
            unit=self.unit,
            question=self.question,
            content='mywords content'
        )
        self.question.delete()
        self.assertTrue(MyWords.objects.filter(pk=mywords.pk).exists())

    def test_deleting_question_sets_mywords_reference_to_null(self):
        """
        ANM-10: Tests that deleting a question note sets question field to
        null on linked my words note
        """
        mywords = MyWords.objects.create(
            unit=self.unit,
            question=self.question,
            content='my words content'
        )
        self.question.delete()
        mywords.refresh_from_db()
        self.assertIsNone(mywords.question)
