from django.urls import path
from . import views  # Import views from lab_simulator

urlpatterns = [
    path('', views.projectile_view, name='projectile_simulator'),  # Home or simulation page
]
