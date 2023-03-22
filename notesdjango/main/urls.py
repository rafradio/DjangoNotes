from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('new', views.create_new, name="new"),
    path('<int:pk>/edit', views.notesDetailView, name="notes-details"),
    # path('<int:pk>/edit', views.NotesDetailView.as_view(), name="notes-details"),
    path('<int:pk>/delete', views.notesDelete, name="notes-delete"),
]