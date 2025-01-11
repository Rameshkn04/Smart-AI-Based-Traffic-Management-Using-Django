from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('traffic_control.urls')),  # Routes to app's URLs
]
