from django.urls import path

from ship import views

urlpatterns = [
path("", views.index, name='home')
]