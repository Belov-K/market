from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Product

def index(request):
    latest_products_list=Product.objects.order_by('-pub_date')[:5]
    return render(request, 'products/list.html', {'latest_products_list': latest_products_list})

def detail(request, product_id):
    try:
        a=Product.objects.get(id=product_id)
    except:
        raise Http404("Товар не найден")

    latest_review_list=a.review_set.order_by('-id')[:10]
    image_list=a.productimage_set.all()
    print(image_list)
    return render(request, 'products/detail.html', {'product': a, 'latest_review_list': latest_review_list, 'image_list': image_list})

def leave_review(request, product_id):
    try:
        a=Product.objects.get(id=product_id)
    except:
        raise Http404("Товар не найден")

    a.review_set.create(author_name=request.POST['name'], review_text=request.POST['text'])

    return HttpResponseRedirect(reverse('products:detail', args=(a.id,)))