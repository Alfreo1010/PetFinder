import requests
from .models import Localization, Pet
from django.shortcuts import get_object_or_404

def localization(request, pet_id):
    direccion_ip = request.META['REMOTE_ADDR']
    try:
        response_ip = requests.get(f'http://ip-api.com/json/')
    
        data_ip = response_ip.json()
        
        response_coordenadas = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=json&lat={data_ip["lat"]}&lon={data_ip["lon"]}&zoom=18&addressdetails=1')
        data_coordenadas = response_coordenadas.json()

        pet_i = get_object_or_404(Pet, pk=pet_id)

        Localization.objects.create(
            usuario=request.user,
            mascota=pet_i,
            direccion_ip=direccion_ip,
            latitud=data_ip["lat"],
            longitud=data_ip["lon"],
            calle=data_coordenadas["address"]["road"],
            ciudad=data_coordenadas["address"]["city"],
            estado=data_coordenadas["address"]["state"],
            pais=data_coordenadas["address"]["country"]
        )
    except:
        pass