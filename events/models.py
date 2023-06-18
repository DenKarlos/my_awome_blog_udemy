from django.db import models


class Event(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', )

    def __str__(self):
        return f'Событие: {self.text}'
