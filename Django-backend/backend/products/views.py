from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def create(request):
    if(request.method=='POST'):
        productdata=json.loads(request.body.decode('utf-8'));
        title=productdata['title']
        description=productdata['description']
        Productcard=Product(
            title=title,
            description=description
        )
        Productcard.save()
        return JsonResponse({'success' : 'Object created successfully','title' : title, 'description' : description},status=200)
@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def update(request):
    if(request.method=='PUT'):
        productdata=json.loads(request.body.decode('utf-8'));
        id=productdata['id']
        title=productdata['title']
        description=productdata['description']
        Productcard=Product.objects.get(id=id);
        Productcard.title=title
        Productcard.description=description
        Productcard.save()
        return JsonResponse({'success' : 'Object updated successfully'},status=200)
@csrf_exempt
def load(request):
    if(request.method=='GET'):
     all_records = Product.objects.all()
     return JsonResponse(all_records)
@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def delete(request):
    if(request.method=='DELETE'):
        productid=json.loads(request.body.decode('utf-8'));
        id=productid['id']
        Productcard=Product.objects.get(id=id);
        Productcard.delete()
        return JsonResponse({'success' : 'Object deleted successfully'},status=200)
