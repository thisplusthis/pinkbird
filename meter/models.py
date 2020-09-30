from django.db import models
from django.utils import timezone


class Reading(models.Model):
    date = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField()
    humidity = models.FloatField()
    fan = models.BooleanField(default=False)

    def __str__(self):
        return "%s\n" \
               "Humidity: %s\n" \
               "Temperature: %s\n" \
               "Fan: %s" % (self.date, self.humidity, self.temperature, self.fan)