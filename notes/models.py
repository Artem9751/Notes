from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class TopicModel(models.Model):
    topic_name = models.CharField(max_length=128)

    def __str__(self):
        return self.topic_name


class NoteModel(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    topics = models.ManyToManyField(TopicModel)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])



