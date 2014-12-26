from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse  # Http404
from django.core.urlresolvers import reverse
from appsoc.forms import RegisterForm, LoginForm
# permission_required, user_passes_test
from django.contrib.auth.decorators import login_required
from mongoengine.django.auth import User
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from mongoengine.queryset import DoesNotExist

from appsoc import params
# import tasks


def index(request):
    # p = tasks.add.delay(5, 6)
    color = params.colors['home']
    return render(request, 'appsoc/index.html', {'color': color})


def github(request):
    return render(request, 'appsoc/github.html', {})


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            logout(request)

    register_form = RegisterForm()
    color = params.colors['register']

    errors = []

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            try:
                # if register_form.cleaned_data['password'] != register_form.cleaned_data['confirm']:
                #     raise ValidationError('Passwords do not match')

                member = User()
                # member.username = register_form.cleaned_data['name']
                member.email = register_form.cleaned_data['email']
                # member.password = str(register_form.cleaned_data['password'])
                member.save()
                return render(request, 'appsoc/register.html', {
                    'register_form': register_form, 'success': 'You have successfully been added to the mailing list. We will contact you shortly'})

            except Exception as e:
                errors.append(str(e))
                return render(request, 'appsoc/register.html', {
                    'register_form': register_form, 'errors': errors})

    return render(request, 'appsoc/register.html', {
        'register_form': register_form, 'errors': register_form.errors, 'color': color})

    register_form = RegisterForm()
    return render(request, 'appsoc/register.html', {'register_form': register_form, 'color': color})


def login_view(request):
    login_form = LoginForm()
    errors = []

    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])

            if user.password == request.POST['password']:
                user.backend = params.MONGOENGINE_BACKEND
                login(request, user)

                try:
                    import mongoengine
                    assert isinstance(user, mongoengine.django.auth.User)
                except Exception:
                    raise Exception

                if user:
                    return HttpResponseRedirect(reverse('github'))
                else:
                    errors.append('Oops! something went wrong. please refresh')
            else:
                errors.append('Invalid login')
        except DoesNotExist:
            errors.append('Invalid login')
        except Exception as e:
            return HttpResponse(str(e))

    return render(request, 'forum/login_view.html', {'login_form': login_form, 'errors': errors})


def logout_view(request):
    logout(request)
    login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'forum/login_view.html', context)


def about(request):
    color = params.colors['about']
    return render(request, 'appsoc/about.html', {'color': color})


def contact(request):
    color = params.colors['contact']
    mail_account = params.mail_account
    return render(request, 'appsoc/contact.html', {'color': color, 'mail_account': mail_account})


def bank(request):
    color = "#1C8FD1"
    return render(request, 'appsoc/ideabank.html', {'color': color})


def learn(request):
    color = params.colors['learn']
    return render(request, 'appsoc/learn.html', {'color': color})
