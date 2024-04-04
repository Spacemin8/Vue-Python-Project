from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize

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
        return JsonResponse({'success' : 'Object created successfully','title' : title, 'description' : description,'id':Productcard.id},status=200)
@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def update(request,id):
    Productcard=Product.objects.get(id=id);
    if(request.method=='PUT'):
        productdata=json.loads(request.body.decode('utf-8'));
       
        title=productdata['title']
        description=productdata['description']
        Productcard.title=title
        Productcard.description=description
        Productcard.save()
        return JsonResponse({'success' : 'Object updated successfully'},status=200)
@csrf_exempt
def load(request):
    if(request.method=='GET'):
        all_records = list(Product.objects.values())
        return JsonResponse(all_records,safe=False)
@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def delete(request,id):
    Productcard=Product.objects.get(id=id);
    if(request.method=='DELETE'):
        Productcard.delete()
        return JsonResponse({'success' : 'Object deleted successfully'},status=200)
@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def get_Token(request):
   auth_header = request.META.get('HTTP_AUTHORIZATION', '')
   if auth_header.startswith('Bearer '):
     return auth_header.split(' ')[1]
   return None