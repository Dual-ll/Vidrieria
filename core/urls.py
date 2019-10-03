from django.urls import path
from django.conf.urls import url
from .views import index
from . import views

urlpatterns = [
    path('', index, name="home")]