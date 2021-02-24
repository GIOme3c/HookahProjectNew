from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'test_pages/test_page.html')

def index(request):
    return render(request, 'index/index.html')