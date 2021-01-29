from datetime import time
from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=15)

    def __str__(self):
        return f'{self.title} @ {self.start_time.strftime("%I:%M:%S %p")} for {self.duration} minute(s)'
