from django.shortcuts import render
from .models import Notes
from django.shortcuts import get_object_or_404
# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, id):
    note = get_object_or_404(Notes, id=id)
    return render(request, 'notes/notes_detail.html', {'note': note})