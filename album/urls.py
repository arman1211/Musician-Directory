from django.urls import path
from . import views

urlpatterns = [
    path("",views.addAlbum,name='album'),
    path('editalbum/<int:id>', views.editalbum,name='editalbum')
]
