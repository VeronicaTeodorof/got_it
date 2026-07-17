from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'sources/<int:source_pk>/', views.source_detail, name='source-detail'
        ),
    path(
        'sources/<int:source_pk>/delete/',
        views.delete_source,
        name='delete-source'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/',
        views.unit_detail,
        name='unit-detail'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/delete/',
        views.delete_unit,
        name='delete-unit'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/'
        'reference/<int:reference_pk>/',
        views.reference_detail,
        name='reference-detail'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/reference/create/',
        views.create_reference,
        name='create-reference'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/reference/'
        '<int:reference_pk>/edit/',
        views.edit_reference,
        name='edit-reference'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/'
        'mywords/<int:mywords_pk>/',
        views.mywords_detail,
        name='mywords-detail'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/mywords/create/',
        views.create_mywords,
        name='create-mywords'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/'
        'question/<int:question_pk>/',
        views.question_detail,
        name='question-detail'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/question/create/',
        views.create_question,
        name='create-question'
    ),
]
