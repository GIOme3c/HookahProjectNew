from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'staffapp/index.html')

def settings(request):
    return render(request, 'staffapp/settings.html')