from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('create/', views.project_create_view, name="create"),
    path('edit/<int:pk>/', views.project_edit_view, name="edit"),
    path('delete/<int:pk>/', views.project_delete_view, name="delete"),
]
