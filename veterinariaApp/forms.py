from django import forms
from django.forms import ModelForm
from .models import Veterinaria

class VeterinariaForm(forms.Form):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    FechaAtencion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    def clean_nombre(self):
        nombre = self.cleaned_data.get['nombre']
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre

    def clean_dueño(self):
        motivo = self.cleaned_data.get['motivo']
        if len(motivo) < 4:
            raise forms.ValidationError("El motivo debe tener al menos 4 caracteres")
        return motivo

    def clean_edad(self):
        diagnostico = self.cleaned_data.get['diagnostico']
        if len(diagnostico) < 4:
            raise forms.ValidationError(" El diagnostico debe ser mayor a 4")
        return diagnostico

    def cleaned_descripcion(self):
        tratamiento = self.cleaned.get['tratamiento']
        if len(tratamiento) < 4:
            raise forms.ValidationError(" El tratamiento debe tener al menos 4 caracteres")
        return tratamiento

    def cleaned_descripcion(self):
        observacion = self.cleaned.get['observacion']
        if len(observacion) < 4:
            raise forms.ValidationError(" La observacion debe tener al menos 4 caracteres")
        return observacion


class VeterinariaForm(ModelForm):
    class Meta:
        model = Veterinaria
        fields ='__all__'
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    FechaAtencion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get['nombre']
    #     if len(nombre) < 4:
    #         raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
    #     return nombre

    # def clean_dueño(self):
    #     motivo = self.cleaned_data.get['motivo']
    #     if len(motivo) < 4:
    #         raise forms.ValidationError("El motivo debe tener al menos 4 caracteres")
    #     return motivo

    # def clean_edad(self):
    #     diagnostico = self.cleaned_data.get['diagnostico']
    #     if len(diagnostico) < 4:
    #         raise forms.ValidationError(" El diagnostico debe ser mayor a 4")
    #     return diagnostico

    # def cleaned_descripcion(self):
    #     tratamiento = self.cleaned.get['tratamiento']
    #     if len(tratamiento) < 4:
    #         raise forms.ValidationError(" El tratamiento debe tener al menos 4 caracteres")
    #     return tratamiento

    # def cleaned_descripcion(self):
    #     observacion = self.cleaned.get['observacion']
    #     if len(observacion) < 4:
    #         raise forms.ValidationError(" La observacion debe tener al menos 4 caracteres")
    #     return observacion

# class DueñoForm(forms.Form):

#     nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    
#     def clean_nombre(self):
#         nombre = self.cleaned_data.get['nombre']
#         if len(nombre) < 4:
#             raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
#         return nombre

# class DueñoForm(ModelForm):
#     class Meta:
#         model = Dueño
#         fields ='__all__'
#     nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))