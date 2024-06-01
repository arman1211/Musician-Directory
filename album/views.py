from django.shortcuts import render,redirect
from . import forms,models

# Create your views here.
def addAlbum(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
    else:

        form = forms.AlbumForm()
    return render(request, 'album.html',{'form': form})

def editalbum(request,id):
    album = models.AlbumModel.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'album.html',{'form': form})