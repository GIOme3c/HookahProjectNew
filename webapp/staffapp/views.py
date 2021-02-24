from django.shortcuts import render, redirect
from django.contrib import auth
#from data.models import Profile

# Create your views here.
def pg_index(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    content = {
       'User':user,
    }

    return render(request, 'staffapp/pg_index.html', content)

def pg_settings(request):
    return render(request, 'staffapp/pg_settings.html')

def pg_session_add(request):
    return render(request, 'staffapp/pg_add_session.html')

def pg_session_end(request, pk=1):
    return render(request, 'staffapp/pg_end_session.html')

def pg_session_init(request, pk=1):
    return render(request, 'staffapp/pg_init_session.html')

def pg_session(request, pk=1):
    return render(request, 'staffapp/pg_session.html')

def pg_session_change(request, pk=1):
    return render(request, 'staffapp/pg_change_session.html')

def pg_session_addorder(request, pk=1):
    return render(request, 'staffapp/pg_add_order.html')