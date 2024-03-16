from django.db import models
from usuarios.models import CustomUser

# Create your models here.

class Pet(models.Model):
    photo = models.ImageField(upload_to='petpics', blank=False)
    name = models.CharField(max_length=255, blank=False)
    breed = models.CharField(max_length=255, blank=True, )
    age = models.IntegerField(blank=True,)
    description = models.TextField(blank=True, )
    pathology = models.TextField(blank=True, )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.breed + ', owner: ' + self.user.username 

class Localization(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Pet, on_delete=models.CASCADE)
    direccion_ip = models.GenericIPAddressField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    hora = models.DateTimeField(auto_now_add=True)
