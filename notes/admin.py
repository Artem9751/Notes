from django.contrib import admin

from .models import NoteModel, TopicModel

admin.site.register(NoteModel)
admin.site.register(TopicModel)