from django.db import models
import datetime

# Create your models here.
class AlbumModel(models.Model):
    albumName = models.CharField(max_length=100)
    releaseDate = models.DateField(default=datetime.datetime.now())
    rating = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.albumName