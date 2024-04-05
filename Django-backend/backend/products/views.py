from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
@api_view(['POST'])
def create(request):
        title=request.data.get('title')
        description=request.data.get('description')
        Productcard=Product(
            title=title,
            description=description
        )
        Productcard.save()
        return JsonResponse({'success' : 'Object created successfully','title' : title, 'description' : description,'id':Productcard.id},status=200)
@api_view(['PUT'])
def update(request,id):
    Productcard=Product.objects.get(id=id);
    title=request.data.get('title')
    description=request.data.get('description')
    Productcard.title=title
    Productcard.description=description
    Productcard.save()
    return JsonResponse({'success' : 'Object updated successfully'},status=200)

@api_view(['GET'])
def load(request):
        all_records = list(Product.objects.values())
        return JsonResponse(all_records,safe=False)

@api_view(['DELETE'])
def delete(request,id):
     Productcard=Product.objects.get(id=id);
     Productcard.delete()
     return JsonResponse({'success' : 'Object deleted successfully'},status=200)

@api_view()
def get_Token(request):
   auth_header = request.META.get('HTTP_AUTHORIZATION', '')
   if auth_header.startswith('Bearer '):
     return auth_header.split(' ')[1]
   return None