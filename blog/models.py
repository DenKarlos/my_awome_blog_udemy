from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    text = models.TextField(null=None, blank=True)
    image = models.ImageField(upload_to='blog_images/', )

    def __str__(self):
        return f'Статья: {self.title}'
