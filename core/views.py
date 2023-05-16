from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'products': products  # Corrigido o nome da variável para 'products'
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    print(f'pk: {pk}')
    # prod = Product.objects.get(id=pk)  # Corrigido o nome do método para 'objects'
    prod = get_object_or_404(Product, id=pk)

    context = {
        'product': prod  # Alterado para singular, pois estamos passando apenas um produto
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
