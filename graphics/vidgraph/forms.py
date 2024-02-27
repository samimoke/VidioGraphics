from django import forms
from django.core.validators import validate_email
from .models import Contactus
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=['name','email','subject','message']
