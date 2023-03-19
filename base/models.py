from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(
        User, related_name='rooms', on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(
        Topic, related_name='rooms', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
