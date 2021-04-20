from django.http import Http404 #Используется для медленного способа(смотри ниже)
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else: 
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request .POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm(request .POST or None)

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)


def product_detail_view(request, my_id):
    # Более быстрый и удобный способ
    obj = get_object_or_404(Product, id=my_id)
    
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    # Более быстрый и удобный способ
    context = {
        'object': obj
    }
    # context = {
    #     'title': obj.title
    #     'description': obj.description
    # }

    return render(request, "products/product_details.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        'object': obj
    }
  

    return render(request, "products/product_delete.html", context)