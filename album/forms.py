from django import forms
from . import models

class AlbumForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    releaseDate = forms.DateField(widget=forms.DateInput({'type': 'date'}))

    class Meta:
        model = models.AlbumModel
        fields = '__all__'