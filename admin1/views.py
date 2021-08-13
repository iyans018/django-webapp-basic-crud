from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mahasiswa.forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):

    return redirect('login')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {
            'title': 'Login Page',
        }

        return render(request, 'login.html', context)


def logout_page(request):
    logout(request)

    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = RegisterUserForm()
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {
            'title': 'Register Page',
            'form': form,
        }

        return render(request, 'register.html', context)


@login_required(login_url='login')
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'header': 'Dashboard',
    }

    return render(request, 'dashboard.html', context)
