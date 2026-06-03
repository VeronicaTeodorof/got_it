from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'sources/<int:source_pk>/', views.source_detail, name='source-detail'
        ),
    path('sources/create_source/', views.create_source, name='create-source'),
    path(
        'sources/<int:source_pk>/edit/', views.edit_source, name='edit_source'
        ),
    path(
        'sources/<int:source_pk>/delete/',
        views.delete_source,
        name='delete_source'
    )
]
