from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registered. Please use another one.')
            else:
                user=form.save()
                profile=Profile.objects.create(user=user)
                profile.save()
                messages.success(request, f'Welcome {username}! Your account has been created')
                return redirect('users:login')

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def logout_action(request):
    logout(request)
    return render(request,'users/logout.html') 

@login_required
def profile(request):
    return render(request,'users/profile.html')