from django import forms
from .models import Pet

class PetsForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['photo', 'name', 'breed', 'age', 'description', 'pathology']
        widgets = {
            'photo': forms.FileInput(attrs={'class':'form-control form-control-lg'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the name of your pet'}),
            'breed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the breed of your pet (Optional)'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please place the age (Optional)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your pet (Optional, but it can help to identify!)'}),
            'pathology': forms.Textarea (attrs={'class': 'form-control', 'placeholder': 'It has a pathology? tell us (Optional)'}),
        }
