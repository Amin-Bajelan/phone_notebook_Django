from django import forms
from .models import User, Contact


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {'username': 'Please enter your username:', 'email': 'Please enter your email:',
                  'password': 'Select password:'}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact', 'phone_number')
        labels = {'contact': 'Please enter contact name:'
            , 'phone_number': 'Please enter phone number:'}
