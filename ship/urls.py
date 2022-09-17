from django.urls import path

from ship import views

urlpatterns = [
path("", views.index, name='home'),
path("tracking", views.tracking_page, name='tracking'),
path('track', views.track_info, name='tracker')
]