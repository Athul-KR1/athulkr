from django import forms
from .models import *
class RegisterForm(form.ModelForm):
    class Meta:
        model=Register
        fields=['username','email','password','image','phone_number']