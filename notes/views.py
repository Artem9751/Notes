from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NoteModel


class NoteListView(ListView):
    model = NoteModel
    template_name = 'note_list.html'


class NoteDetailView(DetailView):
    model = NoteModel
    template_name = 'note_detail.html'


class NoteUpdateView(UpdateView):
    model = NoteModel
    fields = ('title', 'body',)
    template_name = 'note_edit.html'


class NoteDeleteView(DeleteView):
    model = NoteModel
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')
