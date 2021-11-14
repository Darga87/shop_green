from django.shortcuts import render, redirect
from .models import *
from .forms import ProductForm


def index(request):
    
    product = Product.objects.all()
    return render(request, 'main/index.html', {'title': product, 'product': product})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма ввода не верна'

    

    form = ProductForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html',context)