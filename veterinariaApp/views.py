from django.shortcuts import render,redirect
from veterinariaApp.models import Veterinaria
from .forms import VeterinariaForm
from django.db.models import Avg, Max, Min, Sum 



# Create your views here.
def index(request):
    return render (request, 'index.html',)



def VeterinariaDataView(request):
    
    # VeterinariaDataView = VeterinariaDataView.objects.all().order_by('valor')
    # suma = VeterinariaDataView.objects.all().aggregate(Sum('valor'))
    # maximo = VeterinariaDataView.objects.all().aggregate(Max('valor'))
    # minimo = VeterinariaDataView.objects.all().aggregate(Min('valor'))

    listapacientes = Veterinaria.objects.all()
    data = {'veterina': listapacientes}
    return render(request, 'veterinaria.html', data)





def crearPaciente(request):
    form = VeterinariaForm()
    if (request.method =='POST'):
        form = VeterinariaForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            pacien = form.cleaned_data
            """crear el objeto paciente"""
            paciente = Veterinaria(
                nombre=pacien['nombre'],
                FechaAtencion = pacien['FechaAtencion'],
                motivo=pacien['motivo'],
                diagnostico=pacien['diagnostico'],
                tratamiento=pacien['tratamiento'], 
                observacion=pacien['observacion'],
                valor= pacien['valor']
            )
            print("datos validos")
            paciente.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/veterinaria')

    data={'form': form, 'titulo': 'Crear paciente'}
    return render(request,'crearPaciente.html', data)





def eliminarPaciente(request, id):
    paciente = Veterinaria.objects.get(id=id)
    paciente.delete()
    return redirect('/veterinaria')

def editarPaciente(request, id):
    paciente = Veterinaria.objects.get(id=id)
    form = VeterinariaForm(instance=paciente)
    if (request.method =='POST'):
        form = VeterinariaForm(request.POST, instance=paciente)
        if (form.is_valid()):
            form.save()
            return redirect('/veterinaria')
    data={'form': form, 'titulo': 'Editar paciente'}
    return render(request,'crearPaciente.html', data)


# def DueñoDataView(request):
#     listadueño = Dueño.objects.all()
#     data = {'due': listadueño}
#     return render(request, 'dueño.html', data)

# def crearDueño(request):
#     form = Dueño.Form()
#     if (request.method =='POST'):
#         form = DueñoForm(request.POST)
#         if (form.is_valid()):
            
#             """Rescatar los datos del formulario"""
#             due = form.cleaned_data
#             """crear el objeto paciente"""
#             dueño = Dueño(
#                 nombre=due['nombre'],
#                 edad= due['edad']
#             )
#             print("datos validos")
#             dueño.save()
#             """Limpiar el formulario"""
#             form = ''
#             return redirect('/dueño')

#     data={'form': form, 'titulo': 'Crear dueño'}
#     return render(request,'dueño.html', data)

# def eliminarDueño(request, id):
#     dueño = Dueño.objects.get(id=id)
#     dueño.delete()
#     return redirect('/dueño')

# def editarDueño(request, id):
#     dueño = Dueño.objects.get(id=id)
#     form = DueñoForm(instance=dueño)
#     if (request.method =='POST'):
#         form = DueñoForm(request.POST, instance=dueño)
#         if (form.is_valid()):
#             form.save()
#             return redirect('/dueño')
#     data={'form': form, 'titulo': 'Editar dueño'}
#     return render(request,'cdueño.html', data)