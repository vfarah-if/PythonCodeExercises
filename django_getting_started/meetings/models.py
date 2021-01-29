from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f'({self.id}) {self.title}'
