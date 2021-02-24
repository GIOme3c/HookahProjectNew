from django.shortcuts import render

# Create your views here.
def pg_index(request):
    return render(request, 'staffapp/pg_index.html')

def pg_settings(request):
    return render(request, 'staffapp/pg_settings.html')

def pg_session_add(request):
    return render(request, 'staffapp/pg_add_session.html')