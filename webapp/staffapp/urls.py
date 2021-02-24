from django.urls import path
from . import views

urlpatterns = [
    path('', views.pg_index, name="staffapp"),
    path('settings/', views.pg_settings, name="staffapp-setting"),
    path('session/<int:pk>/', views.pg_session, name="session"),
    path('session/add/', views.pg_session_add, name="session-add"),
    path('session/<int:pk>/end/', views.pg_session_end, name="session-end"),
    path('session/<int:pk>/change/', views.pg_session_change, name="session-change"),
    path('session/<int:pk>/init/', views.pg_session_init, name="session-init"),
    path('session/<int:pk>/addorder/', views.pg_session_addorder, name="session-addorder"),

]