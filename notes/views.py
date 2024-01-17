from django.shortcuts import render
from .models import Notes
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes" # default is objects
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


# def detail(request, id):
#     note = get_object_or_404(Notes, id=id)
#     return render(request, 'notes/notes_detail.html', {'note': note})