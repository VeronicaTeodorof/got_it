from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'sources/<int:source_pk>/', views.source_detail, name='source-detail'
        ),
    path(
        'sources/<int:source_pk>/edit/', views.edit_source, name='edit_source'
        ),
    path(
        'sources/<int:source_pk>/delete/',
        views.delete_source,
        name='delete_source'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/',
        views.unit_detail,
        name='unit-detail'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/edit/',
        views.edit_unit,
        name='edit-unit'
    ),
    path(
        'sources/<int:source_pk>/units/<int:unit_pk>/delete/',
        views.delete_unit,
        name='delete-unit'
    )
]
