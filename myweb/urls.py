from django.urls import path
from . import views


urlpatterns = [
    path('lover', views.lover, name='lover')
]
