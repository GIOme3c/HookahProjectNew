from django.shortcuts import render

# Create your views here.
def pageLogin(request):
    return render(request, 'test_pages/test_page.html')