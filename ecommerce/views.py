from django.shortcuts import render
from django.http import HttpResponse

def ecommerce_index_view(request):
    return HttpResponse("Welcom to 6410742552 artit luanghiranvut view")
# Create your views here.

def item_view(request, item_id):   
    context_data = {"item_id": item_id}
    return render(request, 'index.html',context= context_data)