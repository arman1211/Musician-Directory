from django.db import models
from album.models import AlbumModel
# Create your models here.
class MusicianModel(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    instrumentType = models.CharField(max_length=50)
    album = models.ForeignKey(AlbumModel, on_delete=models.CASCADE)