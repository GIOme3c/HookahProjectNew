from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="staffapp"),
    path('settings/', views.settings, name="staffapp-setting"),
]