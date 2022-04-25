from django.shortcuts import render, redirect, get_object_or_404
from app.forms import registroForm, productoForm
from .models import registro

def home(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def blog(request):
    return render(request, 'app/blog.html')    

def portfolio(request):
    return render(request, 'app/portfolio.html') 

def registros(request):
    data = {

        'form': registroForm()

    }
    
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "consulta guardada"
        else:
            data["form"] = formulario
    return render(request, 'app/contact.html', data) 

def agregar_producto(request):
    data = {

        'form': productoForm()

    }
    
    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "consulta guardada"
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)

def listar_producto(request):
    productos = registro.objects.all() 

    data={

         'registro': productos
    }   

    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(registro, id=id)

    data = {
        'registro': registroForm(instance=producto)

    }

    if request.method == 'POST':
        formulario = registroForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)    

def eliminar_producto(request, id):
    
    producto = get_object_or_404(registro, id=id)
    producto.delete()
    return redirect(to="listar_producto")