from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
class Source(models.Model):
    class SourceType(models.TextChoices):
        # Labels use plain strings;
        # wrap with _() from gettext_lazy if i18n is added
        COURSE = 'course', 'Course'
        BOOK = 'book', 'Book'
        WEBSITE = 'website', 'Website'
        VIDEO = 'video', 'Video'
        PODCAST = 'podcast', 'Podcast'
        DOCUMENTATION = 'docs', 'Documentation'
        ARTICLE = 'article', 'Article'
        OTHER = 'other', 'Other'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sources'
        )
    source_type = models.CharField(max_length=20, choices=SourceType.choices)
    source_name = models.CharField(max_length=255)

    # null=True is intentional here
    # author is genuinely absent for some source types
    # (e.g. websites, docs). When filtering by author, use isnull=True/False.
    # clean_source_author() in SourceForm ensures
    # empty submissions are saved as None.
    source_author = models.CharField(max_length=100, blank=True, null=True)

    source_creation_date = models.DateTimeField(auto_now_add=True)
    source_last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.source_author:
            return f"{self.source_name} by {self.source_author}"
        return self.source_name

    class Meta:
        constraints = [
            # prevents duplicate source names per user,
            #  enforced at database level
            models.UniqueConstraint(
                fields=['user', 'source_name'], name='unique_source_per_user'
                ),

            # prevents invalid source types from being saved,
            # even if form validation is bypassed
            models.CheckConstraint(
                condition=models.Q(
                    source_type__in=[
                        'book', 'article', 'website', 'video',
                        'podcast', 'course', 'docs', 'other'
                    ]
                ),
                name='valid_source_type'
            )
        ]


class Unit(models.Model):
    """
    A unit created by the user inside a source,
    a second level container.
    """
    source = models.ForeignKey(
        Source, on_delete=models.CASCADE, related_name='units'
        )
    unit_name = models.CharField(max_length=255)
    unit_last_modified_date = models.DateTimeField(auto_now=True)
    unit_order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.unit_name

    class Meta:
        constraints = [
            # prevents duplicate unit names per source,
            #  enforced at database level
            models.UniqueConstraint(
                fields=['source', 'unit_name'], name='unique_unit_per_source'
                )
        ]


class Note(models.Model):
    """
    An abstract base model for all types of notes
    """
    unit = models.ForeignKey(Unit,
                             on_delete=models.CASCADE,
                             related_name='%(class)s_notes')
    title = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=10000)
    order = models.PositiveIntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        if self.title:
            return self.title
        return f"{self.__class__.__name__} - {self.unit}"


class Reference(Note):
    """
    A note anchored in the raw source material
    """
    location = models.CharField(
        max_length=255,
        help_text='stores location on source material: page, timestamp, url',
        blank=True
        )


class Question(Note):
    """
    A note capturing a gap in understanding ideas captured in reference notes,
    or adding own questions derived or related to the studied material
    """

    reference = models.ForeignKey(Reference,
                                  on_delete=models.SET_NULL,
                                  related_name='%(class)s_notes',
                                  null=True,
                                  blank=True)


class MyWords(Note):
    """
    A note explaining in own words ideas captured in reference notes,
    or adding own ideas related to the studied material
    """
    reference = models.ForeignKey(Reference,
                                  on_delete=models.SET_NULL,
                                  related_name='%(class)s_notes',
                                  null=True,
                                  blank=True)

    question = models.ForeignKey(Question,
                                 on_delete=models.SET_NULL,
                                 related_name='%(class)s_notes',
                                 null=True,
                                 blank=True)
