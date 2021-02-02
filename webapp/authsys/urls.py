from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.pageLogin, name="login"),
    path('logout/', views.pageLogout, name="logout"),
    path('autherror/', views.pageAuthError, name="autherror"),
]