from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from pets.models import Pet
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('pets:mypets')
        except ValueError:
            return render(request, 'register.html', {
            'form': form,
            'error': 'Please provide valid data'
            })
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pets:mypets')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('usuarios:login')

User = get_user_model()

def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    pets = Pet.objects.filter(user=user)

    context = {
        'user': user,
        'pets': pets,
        'current_user': request.user,
    }
    return render(request, 'profile.html', context)