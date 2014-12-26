from django import forms
from .models import InsToner, Mantenimiento


class ReciboForm(forms.Form):
    marca = forms.CharField(widget=forms.TextInput())
    modelo = forms.CharField(widget=forms.TextInput())
    serie = forms.CharField(widget=forms.TextInput())
    fecha_inicial = forms.CharField(widget=forms.TextInput())
    fecha_final = forms.CharField(widget=forms.TextInput())
    contador_inicial = forms.CharField(widget=forms.TextInput())
    contador_final = forms.CharField(widget=forms.TextInput())


class InsTonerForm(forms.ModelForm):
    class Meta:
        model = InsToner


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento