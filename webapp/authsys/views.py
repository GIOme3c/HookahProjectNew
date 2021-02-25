from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def pageLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if request.user.is_staff:  
                return redirect('adminapp')
            else:
                return redirect('staffapp')
        else:
            messages.error(request, 'Неправильный введен логин или пароль.')
    
    return render(request, 'authsys/login_new.html')

def pageLogout(request):
    logout(request)
    return render(request, 'authsys/logout.html')

def pageRegister(request):
    pass

def pageAuthError(request):
    return render(request, 'authsys/error.html')