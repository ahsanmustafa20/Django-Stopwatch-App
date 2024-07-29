from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
# Create your models here.

class Stopwatch(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    elapsed_time = models.DurationField(default=timedelta())
    is_running = models.BooleanField(default=False)


class Lap(models.Model):
    stopwatch = models.ForeignKey(Stopwatch, on_delete=models.CASCADE)
    lap_time = models.DurationField(default=timedelta())
    created_at = models.DateTimeField(auto_now_add=True)
