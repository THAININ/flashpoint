from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'})) #deixo o resto pra galera do front
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "birth_date")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'birth_date', 'bio')