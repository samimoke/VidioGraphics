from django import forms
from django.core.validators import validate_email
from .models import Contactus
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=['name','email','subject','message']
class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
    # last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), validators=[validate_email])
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), validators=[validate_email])
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
        
    
    

    class Meta:
        model = User
        
        fields = ('first_name','username','email', 'password1', 'password2')
class UserLoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control',
    #                                                         'placeholder':'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'password',
                                                                 'id': 'login-pwd'}))