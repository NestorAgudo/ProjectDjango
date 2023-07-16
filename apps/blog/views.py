from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html')

def categoria(request):
    return render(request, 'blog/categoria.html')

def autor(request):
    return render(request, 'blog/autor.html')

def articulo(request):
    return render(request, 'blog/articulo.html')

def archivo(request):
    return render(request, 'blog/archivo.html')