from django.db import models

class Band(models.Model):
    title = models.CharField(max_length=200, unique=True)
    origin = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.title