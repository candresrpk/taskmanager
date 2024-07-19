from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def logIniew(request):
    
    context = {
        'form': AuthenticationForm
    }
    
    if request.method == 'GET':
        return render(request, 'users/signin.html', context)
    else:
        
        user = authenticate(request, username= request.POST['username'], password = request.POST['password'])
        
        if user is None:
            context['error'] = 'Invalid credentials'
            return render(request, 'users/signin.html', context)
        
        login(request, user)
        return redirect('tasks:tasks')
        

    

@login_required
def logOutView(request):
    logout(request)
    return redirect('home')


def signUpView(request):
    
    form = UserCreationForm
    
    context = {
        'form': form,
    }
    
    if request.method == 'GET':
        return render(request, 'users/signup.html', context)
    
    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password1']
            )
            user.save()
            login(request, user)
            return redirect('tasks:tasks')
        
        except IntegrityError:
            context['error'] = 'User already exists'
            return render(request, 'users/signup.html', context)
        except Exception as e:
            context['error'] = e
            return render(request, 'users/signup.html', context)
    else:
        context['error'] = 'Passwords do not match'
        return render(request, 'users/signup.html', context)

