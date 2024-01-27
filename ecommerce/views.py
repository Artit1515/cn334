from django.shortcuts import render
from django.http import HttpResponse

def ecommerce_index_view(request):
    return HttpResponse("Welcom to 6410742552 artit luanghiranvut view")
# Create your views here.

def item_view(request, item_id):   
    context_data = {"item_id": item_id}
    return render(request, 'index.html',context= context_data)

def homepage(request):   
    return render(request,"Homepage.html")

def productpage(request):   
    return render(request,"Productpage.html")

def checkoutpage(request):   
    return render(request,"Checkoutpage.html")

def contactpage(request):   
    return render(request,"Contactpage.html")

def categorypage(request):
    return render(request,"Categorypage.html")