from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse  # Http404
from django.core.urlresolvers import reverse
from appsoc.forms import RegisterForm, LoginForm, EventsRegisterForm
# permission_required, user_passes_test
from mongoengine.django.auth import User
from django.contrib.auth import login, logout
from mongoengine.queryset import DoesNotExist
from appsoc.models import Member, Gsa, IOS

from appsoc import params
# import tasks


def index(request):
    # p = tasks.add.delay(5, 6)
    color = params.colors['home']
    return render(request, 'appsoc/index.html', {'color': color})


def github(request):
    return render(request, 'appsoc/github.html', {})


def register(request, **kwargs):
    register_form = RegisterForm()

    errors = []

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            try:
                member = Member()
                member.email = register_form.cleaned_data['email']
                member.save()
                return HttpResponseRedirect(reverse('register_success', args=(), kwargs={'success': 'success'}))

            except Exception as e:
                errors.append(e)
                return render(request, 'appsoc/register.html', {
                    'register_form': register_form, 'errors': errors})
        else:
            return render(request, 'appsoc/register.html', {'register_form': register_form, 'errors': errors})

    if kwargs.get('success', None):
        success = 'You have successfully been added to the mailing list. We will contact you shortly'
        print success
    else:
        success = ''

    register_form = RegisterForm()
    return render(request, 'appsoc/register.html', {'register_form': register_form, 'errors': errors, 'success': success})


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


def abc(request, **kwargs):
    message = ''
    if request.method == "POST":
        register_form = EventsRegisterForm(request.POST)
        if register_form.is_valid():
            try:
                member = Gsa()
                member.email = register_form.cleaned_data['email']
                member.event = 'GSA'
                member.save()
                return HttpResponseRedirect(reverse('abc_success', args=(), kwargs={'success': 'success'}))

            except Exception as e:
                message = str(e)
                render(request, 'appsoc/abc.html',
                       {'events': True, 'message': message, 'register_form': register_form})
        else:
            message = register_form['email'].errors
            render(request, 'appsoc/abc.html',
                   {'events': True, 'message': message, 'register_form': register_form})

    if kwargs.get("success", None):
        message = "Success! We have saved your email address and will keep you posted"
    register_form = EventsRegisterForm()
    return render(request, 'appsoc/abc.html', {'events_abc': True, 'message': message, 'register_form': register_form})


def ios(request, **kwargs):
    message = ''
    if request.method == "POST":
        register_form = EventsRegisterForm(request.POST)
        if register_form.is_valid():
            try:
                member = IOS()
                member.email = register_form.cleaned_data['email']
                member.event = 'iOS'
                member.save()
                return HttpResponseRedirect(reverse('ios_success', args=(), kwargs={'success': 'success'}))

            except Exception as e:
                message = str(e)
                render(request, 'appsoc/ios.html',
                       {'events': True, 'message': message, 'register_form': register_form})
        else:
            message = register_form['email'].errors
            render(request, 'appsoc/ios.html',
                   {'events': True, 'message': message, 'register_form': register_form})

    if kwargs.get("success", None):
        message = "Success! We have saved your email address and will keep you posted"
    register_form = EventsRegisterForm(event="ios")
    return render(request, 'appsoc/ios.html', {'events_ios': True, 'message': message, 'register_form': register_form})


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
