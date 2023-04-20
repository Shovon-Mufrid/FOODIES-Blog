from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from Login_App.models import UserProfile

# extra field add
class SignUpForm(UserCreationForm):

    email = forms.EmailField(label='Email Address' ,required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') #default USer 


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]
        







