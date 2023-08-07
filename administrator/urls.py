from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("dashboard/", views.dashboard),
    path('Admin_login/', views.login_view, name='Admin_login'),
    path('register/', views.register_view, name='register'),
    
]
