from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def musicians(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = forms.MusicianForm()
    return render(request, 'musician.html',{'form': form})

def showmusician(request):
    musician = models.MusicianModel.objects.all()
    return render(request, 'home.html', {'musicians': musician})

def editmusician(request,id):
    musician = models.MusicianModel.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'musician.html',{'form': form})

def deletemusician(request,id):
    musician = models.MusicianModel.objects.get(pk=id)
    musician.delete()
    return redirect('home')
