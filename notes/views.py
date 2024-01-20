from django.shortcuts import render
from .models import Notes
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, ListView
from .forms import NotesForm
# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes" # default is modelname_list
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note' # default is modelname lowercased.


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
