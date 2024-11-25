from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#Your Django Forms goes here

#Registration Form
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email', 'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password-repeat', 'placeholder':'Confirm Password'}))



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#User Update Form
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'email', 'placeholder':'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Last Name'}))
    about_author = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id':'message', 'cols':'10', 'rows':'8', 'placeholder':'About'}))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'about_author', 'image']

#Post Form Creation
class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Title'}))
    little_description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Little Description'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id':'message', 'cols':'10', 'rows':'8', 'placeholder':'Description'}))

    class Meta:
        model = Post
        fields = ['title', 'little_description', 'description', 'post_category', 'post_image']

#Form for searching
class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class':'search-bar__input', 'id':'search', 'placeholder':'Make a search...'}))