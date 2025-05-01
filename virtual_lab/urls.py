from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lab_simulator.urls')),  # Set lab_simulator as the default homepage
]
