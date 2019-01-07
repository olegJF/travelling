from django import forms
from .models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Поезд', 
                           widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Введите номер поезда'}))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(),
                                       widget=forms.Select(
                                       attrs={'class': 'form-control',
                                              'placeholder': 'Откуда'}))

    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(),
                                     widget=forms.Select(
                                     attrs={'class': 'form-control',
                                            'placeholder': 'Куда'}))
    travel_time = forms.IntegerField(label='Поезд', 
                                     widget=forms.NumberInput(
                                       attrs={'class': 'form-control',
                                              'placeholder': 'Время в пути'}))

    class Meta(object):
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')

