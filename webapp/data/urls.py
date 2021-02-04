from django.urls import path
from . import views

urlpatterns = [
    path('', views.pageLogin, name="test"),
]