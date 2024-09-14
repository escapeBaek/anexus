from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import user_is_approved, user_is_specially_approved
from django.urls import reverse  # Make sure this is imported

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_approved:
                login(request, user)
                return redirect(reverse('land/home.html'))  # Make sure this matches your URL pattern
            else:
                messages.error(request, 'Your account is not approved. Please contact the administrator.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html', {})

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Your account is pending approval.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Exams view with special approval check
@login_required
@user_is_specially_approved
def exams_view(request):
    return render(request, 'exams.html', {})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
