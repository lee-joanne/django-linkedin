from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Notes
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes" # default is modelname_list
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.author.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note' # default is modelname lowercased.


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form): # called when the form is valid
        self.object = form.save(commit=False) # This line is saving the form data temporarily to self.object without committing it to the database immediately. The commit=False parameter means that it won't save the object to the database just yet.
        self.object.user = self.request.user
        self.object.save() # saves the object directly into database
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'