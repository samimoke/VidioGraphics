from django import forms
from django.core.validators import validate_email
from .models import Contactus, Comment, Subscription
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from .models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=['name','email','subject','message']
class RegistrationForm(UserCreationForm):
    # first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
    # last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
    
    # # username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
    # # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), validators=[validate_email])
    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}), validators=[validate_email])
    # password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        
        fields = ('first_name','last_name','email', 'password1')
class UserLoginForm(AuthenticationForm):
    # email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder':'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'password',
                                                                 'id': 'login-pwd'}))
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('first_name', 'body')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
    )
