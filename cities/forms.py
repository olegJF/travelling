from django import forms

class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')