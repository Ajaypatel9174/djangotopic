from django import forms

class Registrationform(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    contact = forms.IntegerField()
    image = forms.ImageField()
    resume = forms.FileField()