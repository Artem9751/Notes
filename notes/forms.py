from django import forms

from .models import NoteModel


class NoteSearchForm(forms.Form):
    search = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = NoteModel