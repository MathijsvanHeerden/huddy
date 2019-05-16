from django.db import models
from enum import Enum
from datetime import timedelta
# Create your models here.


class MessageInterval(Enum):
    Dagelijks = timedelta(days=1)
    Wekelijks = timedelta(weeks=1)
    Maandelijks = timedelta(weeks=4)


class RepeatedMessage(models.Model):
    messageText = models.TextField()
    messageFilename = models.CharField(null=False, blank=False, max_length=250)
    interval = models.DurationField(choices=[(tag.value, tag.name) for tag in MessageInterval])
    time = models.TimeField()


