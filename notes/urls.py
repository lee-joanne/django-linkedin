from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name='notes_list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='notes_detail'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes_new'),
    path('notes/edit/<int:pk>', views.NotesUpdateView.as_view(), name='notes_update'),
    path('notes/delete/<int:pk>', views.NotesDeleteView.as_view(), name='notes_delete'),
]