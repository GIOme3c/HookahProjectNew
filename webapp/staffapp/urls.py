from django.urls import path
from . import views

urlpatterns = [
    path('', views.pg_index, name="staffapp"),
    path('settings/', views.pg_settings, name="staffapp-setting"),
    path('session/add/', views.pg_session_add, name="session-add"),
]