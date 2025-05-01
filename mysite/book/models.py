from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    user_role = models.CharField(max_length=40, choices=[('admin','admin'),('client','client'),
                                                         ('owner','owner')])


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    organizer = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='organizer')


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event')
    created_at = models.DateTimeField(auto_now_add=True)
