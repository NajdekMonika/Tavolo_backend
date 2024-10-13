from django.db import models
from .utils import generate_random_key
import uuid


class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey('Event', to_field='event_key', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField()
    interests = models.JSONField()
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    flag = models.CharField(max_length=20)
    availability = models.BooleanField(default=True)
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name


class Event(models.Model):
    event_key = models.CharField(max_length=10, unique=True)
    admin_key = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.event_key = generate_random_key(4)
        self.admin_key = generate_random_key(8)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    event_key = models.ForeignKey(Event, to_field='event_key', on_delete=models.CASCADE)
        
    def __str__(self):
        return f"Table {self.number}"

