from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    EXPLORER = 'Explorer'
    TOPIC_FOCUSED = 'Topic focused'
    RESERVED = 'Reserved'
    FLAG_CHOICES = [
        (EXPLORER, 'Explorer'),
        (TOPIC_FOCUSED, 'Topic focused'),
        (RESERVED, 'Reserved'),
    ]

    name = models.CharField(max_length=100)
    interests = models.TextField()
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    flag = models.CharField(max_length=20, choices=FLAG_CHOICES, default=EXPLORER)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='event_logos/')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    number_of_tables = models.PositiveIntegerField()
    event_key = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Table {self.number}"


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
