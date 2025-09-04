from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['itemname', 'itemPrice', 'itemImage']   # fields to include in form
        widgets = {
            'itemname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'itemPrice': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'itemImage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }