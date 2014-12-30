from django.core.exceptions import ValidationError
from mongoengine.django.auth import User
from django.core.validators import RegexValidator
from django import forms
import params


class RegisterForm(forms.Form):
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name = forms.CharField(
        label='Your username', max_length=30, required=False, validators=[alphanumeric])
    email = forms.EmailField(label='Your email', max_length=30, required=True)
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data['name']
        # if name in User.objects.distinct('username'):
        #     raise ValidationError("That username is taken")
        # return name
        raise ValidationError("Sorry! AppSoc's server's are having a little trouble. Please try again at a later date")

    def clean_email(self):
        email = self.cleaned_data['email']
        raise ValidationError("Sorry! AppSoc's server's are having a little trouble. Please try again at a later date")
    #     if email in User.objects.distinct('email'):
    #         raise ValidationError("Email already exists")
    #     email_address = str(email)
    #     for component in params.imperial_college_email_components:
    #         if component in email_address:
    #             return email
    #     raise ValidationError("Email not an Imperial College address")


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
