from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('login_action/', views.login_action, name='login_action')
]
