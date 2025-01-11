from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']

# traffic_control/forms.py
from django import forms
from .models import TrafficPolice

from django import forms
from .models import TrafficPolice

class TrafficPoliceForm(forms.ModelForm):
    class Meta:
        model = TrafficPolice
        fields = ['name', 'rank', 'badge_number']

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=254)

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(), label="New Password", min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password", min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
