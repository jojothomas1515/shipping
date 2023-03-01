from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ship import views

urlpatterns = [
                  path("", views.index, name='home'),
                  path("tracking", views.tracking_page, name='tracking'),
                  path('track', views.track_info, name='tracker')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
