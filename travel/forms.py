from django import forms
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username').strip()
        password = self.cleaned_data.get('password').strip()
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Пароль неверный!')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данный аккаунт отключен')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data
        if data['password'] !=  data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
           
        return data['password2']
