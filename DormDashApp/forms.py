from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

'''
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email', 'password1', 'password2']

'''

class CustomerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )
    email = forms.EmailField(required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = ('phone_number')
        customer.email = ('email')
        return user


class DriverSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit = True):
        user = super().save(commit=False)
        user.is_driver = True
        if commit:
            user.save()
        return user

class ProfileChangeForm(forms.ModelForm):
    phone_number = models.CharField(max_length=15)
    class Meta:
        model = Customer
        fields = ('phone_number',)

'''
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone_number = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email','phone_number']

class UpdateProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['address']

'''
