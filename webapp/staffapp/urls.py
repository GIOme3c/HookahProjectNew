from django.urls import path
from . import views

urlpatterns = [
    path('', views.pg_index, name="staffapp"),
    path('settings/', views.pg_settings, name="staffapp-setting"),
    path('session', views.pg_session, name="session"),
    path('session/add/', views.pg_session_add, name="session-add"),
    path('session/end/', views.pg_session_end, name="session-end"),
    path('session/change/', views.pg_session_change, name="session-change"),
    path('session/init/', views.pg_session_init, name="session-init"),
    path('session/addorder/', views.pg_session_addorder, name="session-addorder"),

]