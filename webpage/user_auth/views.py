from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

@login_required
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username
        })


def auth_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is not None and password is not None:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user_auth:show_user'))

    # Handle authentication failure, maybe show an error message
    return render(request, 'authentication/login.html', {'error_message': 'Invalid username or password'})

        
def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:auth_user')
    else:
        form = UserCreationForm()  # Use UserCreationForm for registration
    return render(request, 'authentication/registration.html',{'form':form})

