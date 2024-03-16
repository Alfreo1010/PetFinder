from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.home, name='home'),
    path('mypets/', views.mypets, name='mypets'),
    path('mypets/notifications', views.notifications, name='notifications'),
    path('mypets/view/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path("mypets/view/<int:pet_id>/mail/", views.correo, name="mail"),
    path('mypets/view/<int:pet_id>/qrcode/', views.create_qr, name='pet_qrcode'),
    path('mypets/edit/<int:pet_id>/', views.pet_edit, name='pet_edit'),
    path('mypets/edit/<int:pet_id>/delete/', views.pet_delete, name='pet_delete'),
    path('mypets/create/', views.create_pets, name='create_pets'),
]