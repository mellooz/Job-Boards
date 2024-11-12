from django import forms

# django support UserCreationForm , we didnt make any table for user in models to connect it with this
# modelform sso we used UserCreationForm and nots that UserCreationForm used when u make signup form
# so u need to hash the password ans some processes , so django who must create the user
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Profile , City

class SignupForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username' , 'email' ,  'password1' , 'password2']
        # if u want to edit first name put 'first_name'
        # fields = ['username' ,'first_name','last_name' , 'email' ,  'password1' , 'password2']




# this 2 forms [UserForm - ProfileForm] used to edit profile and we need to update both tables

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'first_name' ,  'last_name'  ,'email' ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image' , 'city' , 'phone_number']

