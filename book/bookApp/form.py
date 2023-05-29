from django.forms import ModelForm, TextInput,  PasswordInput, EmailInput,  ClearableFileInput, SelectMultiple, Select, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from .models import Post, Comment
from django.forms import ModelForm, TextInput,  PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SingupForm(UserCreationForm):
    email = forms.EmailInput()
    #image = forms.ImageField()
    #first_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
       


class CreatPostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ( 'picture', 'title', 'overview','author','categories',)
       widgets = {
            'picture':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'categories':forms.SelectMultiple(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'overview':forms.Textarea(attrs={'class':'form-control'}),
       }
    

class MassageForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ('comment',)
       widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control'}),
       }