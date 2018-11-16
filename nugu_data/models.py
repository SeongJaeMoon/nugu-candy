from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Calorie(models.Model):
    _id = models.CharField(max_length=200)
    _calroie = models.CharField(max_length=200)
    _text = models.TextField()
    _date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        Calorie.objects.filter(date__lte=timezone.now())\
                       .order_by('created_at')
        return self._id
    