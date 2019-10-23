from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import NoteSearchForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import NoteModel, TopicModel
from django.shortcuts import render
from itertools import chain


class NoteListView(LoginRequiredMixin, ListView):
    model = NoteModel
    template_name = 'note_list.html'
    form_class = NoteSearchForm
    login_url = 'login'

    def post(self, request):
        topic = request.POST.get("search")
        note_list = NoteModel.objects.filter(topics__topic_name=topic)
        return render(request, self.template_name, {'note_list': note_list, 'noteform': NoteSearchForm()})

    def get(self, request):
        notes = NoteModel.objects.all()


        for note in notes:
            a = note.topics.all()
            #notes = notes | a
            print(a)
        print(str(notes.query))
        #fall = {1: notes, 2: topics}
        return render(request, self.template_name, {'notes': notes})


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = NoteModel
    template_name = 'note_detail.html'
    login_url = 'login'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = NoteModel
    fields = ('title', 'body', 'topics')
    template_name = 'note_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = NoteModel
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NoteCreateView(CreateView):
    model = NoteModel
    template_name = 'note_create.html'
    fields = ('title', 'body', 'topics')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
