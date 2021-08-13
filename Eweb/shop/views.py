from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact, Order
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) + (n // 4))
    # allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    # params = {'allProds': allProds}
    # return render(request, 'shop/index.html', params)

#cateregory wise slideshoww
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def traker(request):
    return render(request, 'shop/traker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address1 = request.POST.get("address1", "")
        address2 = request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        phone = request.POST.get("phone", "")
        textarea = request.POST.get("textarea", "")
        order = Order(name=name, email=email, address1=address1, address2=address2, city=city, state=state,phone=phone, textarea=textarea)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
    return render(request, 'shop/checkout.html')




