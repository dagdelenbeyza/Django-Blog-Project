from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'type': "text",
                                     'class': "form-control",
                                     'placeholder': "Name",
                                     'id': "name",
                                     'data-validation-required-message': "Please enter your name."
                                     }),
            'email': TextInput(attrs={'type': "email",
                                      'class': "form-control",
                                      'placeholder': "Email Address",
                                      'id': "email",
                                      'data-validation-required-message': "Please enter your email address."}),
            'message': Textarea(attrs={'rows': "5",
                                       'class': "form-control",
                                       'placeholder': "Message",
                                       'id': "message",
                                       'data-validation-required-message': "Please enter a message."}),
        }
