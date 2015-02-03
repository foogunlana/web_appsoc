from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from pymongo import MongoClient
from django import forms
import params


class RegisterForm(forms.Form):
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    # name = forms.CharField(
    # label='Your username', max_length=30, required=False,
    # validators=[alphanumeric])
    email = forms.EmailField(label='Your email', max_length=50, required=True)
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm = forms.CharField(widget=forms.PasswordInput)

    # def clean_name(self):
    # name = self.cleaned_data['name']
    # if name in User.objects.distinct('username'):
    #     raise ValidationError("That username is taken")
    # return name
    # raise ValidationError(
    # "Sorry! AppSoc's server's are having a little trouble. Please try again at a later date")

    def clean_email(self):
        client = MongoClient(params.MONGO_URI)
        email = self.cleaned_data['email']
        if email in client.appsoc.member.distinct('email'):
            raise ValidationError("You're already signed up!")
        email_address = str(email)
        for component in params.imperial_college_email_components:
            if component in email_address:
                return email
        print "Non Imperial email allowed"
        return email
        # raise ValidationError("Email not an Imperial College address")


class EventsRegisterForm(forms.Form):
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    email = forms.EmailField(label='', max_length=50, required=True,
                             widget=forms.TextInput(attrs={'class': 'trans_input', 'data-validation': 'email'}))

    def clean_email(self):
        client = MongoClient(params.MONGO_URI)
        email = self.cleaned_data['email']
        if email in client.appsoc.gsa.distinct('email'):
            raise ValidationError("Email already exists")
        email_address = str(email)
        for component in params.imperial_college_email_components:
            if component in email_address:
                return email
        print "Non Imperial email allowed"
        return email
        # raise ValidationError("Email not an Imperial College address")


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
