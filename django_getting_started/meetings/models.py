from datetime import time
from django.db import models


class Room(models.Model):
    name = models.TextField(max_length=50)
    floor = models.IntegerField(default=1)
    room = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.name} on floor {str(self.floor)} room {str(self.room)}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=15, verbose_name="Duration (minutes)")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id}-{self.title} @ {self.start_time.strftime("%I:%M:%S %p")} for {self.duration} minutes {self.room_info}'

    @property
    def room_info(self):
        return f'in room {self.room.name}' if self.room is not None else '(online)'
