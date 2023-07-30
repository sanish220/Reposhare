from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class customform(UserCreationForm):
    username= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    password1= forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    )
    password2= forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
    )



