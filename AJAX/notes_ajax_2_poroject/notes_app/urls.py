from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('notes', views.Notes.as_view())
]
