from django.urls import path, re_path, include
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>/', views.user_profile, name='profile'),
]