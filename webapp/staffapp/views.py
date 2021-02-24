from django.shortcuts import render

# Create your views here.
def pg_index(request):
    return render(request, 'staffapp/pg_index.html')

def pg_settings(request):
    return render(request, 'staffapp/pg_settings.html')

def pg_session_add(request):
    return render(request, 'staffapp/pg_add_session.html')

def pg_session_end(request):
    return render(request, 'staffapp/pg_end_session.html')

def pg_session_init(request):
    return render(request, 'staffapp/pg_init_session.html')

def pg_session(request):
    return render(request, 'staffapp/pg_session.html')

def pg_session_change(request):
    return render(request, 'staffapp/pg_change_session.html')

def pg_session_addorder(request):
    return render(request, 'staffapp/pg_add_order.html')