from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class register(UserCreationForm):
    
    email = forms.EmailField(max_length=200, help_text="Please enter a valid email")
    
    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    #clean the mail and name of the account in registration
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user_object = User.objects.get(email = email)
        except Exception:
            return email
        raise forms.ValidationError(email + " is used")
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user_object = User.objects.get(username = username)
        except Exception:
            return username
        raise forms.ValidationError(username + "is used")
