from django.urls import path
from . import views

app_name = 'station'
urlpatterns = [
    path('', views.index, name='ListCS')
]
