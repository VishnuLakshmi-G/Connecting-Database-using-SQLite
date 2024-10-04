# five/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('exercise/new/', views.exercise_create, name='exercise_create'),
    path('exercise/<int:pk>/edit/', views.exercise_update, name='exercise_update'),
    path('exercise/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
]
