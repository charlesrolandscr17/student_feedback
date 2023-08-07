from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name = "signin"),
    path('index/', views.index, name='index'),
    path('get_year_of_study/', views.year_of_study, name='get_year_of_study'),    
    path('get_semester/', views.semester, name='get_semester'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home' ),
    path('login/', views.login, name='login' ),
    path('logout/', views.logout, name='logout' ),
    path('profile/', views.profile, name='profile' ),
    path('register/', views.register, name='register' ),
    path('get_course_units/', views.get_course_units, name='get_course_units'),

    path('index/form.html', views.form, name='form'),
    path('form/', views.multi_step_form_view, name='feedback'),
]
