from django import forms
from .models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', 
                           widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Введите название города'}))

    class Meta(object):
        model = City
        fields = ('name', )
