from .models import Product
from django.http import JsonResponse
from rest_framework.decorators import api_view
from user.authorization import token_required


@api_view(['POST'])
@token_required
def create(request):
    # if get_Token(request):
        title=request.data.get('title')
        description=request.data.get('description')
        Productcard=Product(
            title=title,
            description=description
        )
        Productcard.save()
        return JsonResponse({'success' : 'Object created successfully','title' : title, 'description' : description,'id':Productcard.id},status=200)
    # return JsonResponse({'message' : 'UnAuthorized User'})
@api_view(['PUT'])
@token_required
def update(request,id):
    Productcard=Product.objects.get(id=id);
    title=request.data.get('title')
    description=request.data.get('description')
    Productcard.title=title
    Productcard.description=description
    Productcard.save()
    return JsonResponse({'success' : 'Object updated successfully'},status=200)

@api_view(['GET'])
@token_required
def load(request):
    auth_header = request.META.get('Authorization', '')
    print(auth_header)
    all_records = list(Product.objects.values())
    return JsonResponse(all_records,safe=False)

@api_view(['DELETE'])
@token_required
def delete(request,id):
     Productcard=Product.objects.get(id=id);
     Productcard.delete()
     return JsonResponse({'success' : 'Object deleted successfully'},status=200)