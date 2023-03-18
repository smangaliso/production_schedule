
# Create your models here.
from django.db import models


class Machine(models.Model):
    serial_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.serial_number


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_code = models.CharField(max_length=20)

    def __str__(self):
        return self.event_code


class ProductionSchedule(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.DurationField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.machine} - {self.event}"

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = self.end_time - self.start_time

        if not self.end_time:
            self.end_time = self.start_time + self.duration

        super().save(*args, **kwargs)

