from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sources/', views.sources_list, name='sources-list'),
    path(
        'sources/<int:source_pk>/', views.source_detail, name='source-detail'
        ),
]
