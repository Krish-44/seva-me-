from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import UserRegForm
from .models import Userregistration


def login_page(request):
    context = {'message': 'Invalid Credentials......'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Userregistration.objects.filter(Q(username=username), Q(password=password))
        if data:
            return redirect('services')
        else:
            return render(request, 'users/login_page.html', context)
    return render(request, 'users/login_page.html')


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            # Check if 'password' and 'repassword' match before saving
            if form.cleaned_data['password'] == form.cleaned_data['repassword']:
                user = form.save()
                # Log in the user after successful registration
                return redirect('services')
            else:
                # Handle password mismatch error here, e.g., by adding an error to the form
                form.add_error('repassword', 'Passwords do not match')
        # If the form is not valid, or passwords do not match, render the registration form again
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('homepage')  # Redirect to your desired page after logout
