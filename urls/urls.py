from django.urls import path
from . import views

urlpatterns = [
    path('urls/', views.urls_dir, name='urls_dir'),
]