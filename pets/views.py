from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from io import BytesIO
from django.contrib.auth.decorators import login_required
import qrcode
from usuarios.models import CustomUser
from django.core.mail import send_mail
from .forms import PetsForm
from .models import Pet, Localization
from .utils import localization
from store.utils import cartData

# Create your views here.
def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'home.html', context)

@login_required
def mypets(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'mypets.html', {'pets': pets})

@login_required
def create_pets(request):
    if request.method == 'GET':
        return render(request, 'create_pets.html', {
        'form': PetsForm
        })
    else:
        try:
            form = PetsForm(request.POST, request.FILES)
            new_pet = form.save(commit=False)
            new_pet.user = request.user
            new_pet.save()
            return redirect('pets:mypets')
        except ValueError:
            return render(request, 'create_pets.html', {
            'form': PetsForm,
            'error': 'Please provide valid data'
            })

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    localization(request, pet_id)

    return render(request, 'pet_detail.html', {
        'pet': pet,
    })

@login_required
def pet_edit(request, pet_id):
    if request.method == 'GET':
        pet = get_object_or_404(Pet, pk=pet_id, user=request.user)
        form = PetsForm(instance=pet)
        return render(request, 'pet_edit.html', {
            'pet': pet,
            'form': form
        })
    else:
        try:
            pet = get_object_or_404(Pet, pk=pet_id, user=request.user)
            form = PetsForm(request.POST, request.FILES,  instance=pet)
            form.save()
            return redirect('pets:mypets')
        except ValueError:
            return render(request, 'pet_edit.html', {
            'pet': pet,
            'form': form,
            'error': 'Error updating information'
            })

@login_required        
def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id, user=request.user)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets:mypets')

def create_qr(request, pet_id):

    url = request.build_absolute_uri()

    img = qrcode.make(url)
    buf = BytesIO()
    img.save(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')


    return response

@login_required
def notifications(request):
    notificacion = Localization.objects.filter(usuario=request.user).order_by('-hora__hour','-hora__day', '-hora__month')
    return render(request, 'notifications.html', {'notifys': notificacion})

def correo(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    user = CustomUser.objects.get(username=pet.user.username)
    victoria = Localization.objects.filter(usuario=user).order_by('-hora').first()
    owner_email = pet.user.email
    owner_name = pet.user.get_full_name()
    pet_name = pet.name
    subject = f"Reciente escaneo de {pet_name}"
    message = f"Hola {owner_name}, \n\nTu mascota {pet_name} fue reciente mente escaneada en: \n\n{victoria.calle}, {victoria.ciudad}, {victoria.estado}, {victoria.pais} el {victoria.hora} \n\nNuestros mejores deseos, \nEl equipo ejecutivo de PetFinder"

    send_mail(
        subject,
        message,
        'petfinder69@gmail.com',
        [owner_email],
        fail_silently=False,
    )
    
    return redirect('pets:pet_detail', pet_id=pet_id)