from django.shortcuts import render
from .models import Product,Contact,Orders
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 2 + ceil((n / 2) - (n // 2))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request): 
      if request.method=='POST': 
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        
        contact=Contact(name=name,email=email,number=number,message=message)
    
        contact.save()
        messages.success(request,'Details submitted !')
        
      return render(request,'shop/contact.html')
    

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request,myid):
  
  product = Product.objects.filter(id=myid)
  return render(request,'shop/productView.html',{'product':product[0]})

def checkout(request):
  if request.method=="POST":
    items_json= request.POST.get('itemsJson', '')
    name=request.POST.get('name', '')
    email=request.POST.get('email', '')
    address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
    city=request.POST.get('city', '')
    state=request.POST.get('state', '')
    zip_code=request.POST.get('zip_code', '')
    order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code)
    order.save()
    thank=True
    id=order.order_id
    return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
  return render(request, 'shop/checkout.html')
 

def cart(request): 
  return render(request,'shop/cart.html')