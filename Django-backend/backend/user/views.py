from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import jwt
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Token

@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
# Create your views here.
def signup(request):
    if(request.method=='POST'):
        payload=json.loads(request.body.decode('utf-8'));
        username = payload['username']
        email = payload['email']
        password = payload['password']
        userExist=User.objects.filter(email=email)
        if not (username and email and password):
          return JsonResponse({'error': 'Missing userdata.'},status=400)
        if(userExist):
          return JsonResponse({'error': 'User already Existed.'},status=400)
        hashed_password = make_password(password)
          # Create an instance of the model with the data
        data = User(
            username=username,
            email=email,
            password=hashed_password,
            # Set other fields as needed
        )
        data.save()
        return JsonResponse({'message': 'UserData saved successfully'},status=200)

@csrf_exempt  # Use this decorator to exempt the view from CSRF verification
def login(request):
    if(request.method=='POST'):
        credentials=json.loads(request.body.decode('utf-8'));
        email=credentials['email']
        password=credentials['password']
        userExist=User.objects.get(email=email)
        Asecretkey="accesstokensecret"
        Rsecretkey="refreshtokensecret"
        if not (email and password):
          return JsonResponse({'error': 'Missing userdata.'},status=400)
        if check_password(password,userExist.password):
          accesstoken=jwt.encode(credentials,Asecretkey,algorithm="HS256")
          refreshtoken=jwt.encode(credentials,Rsecretkey,algorithm="HS256")
          data=Token(
            accesstoken=accesstoken,
            refreshtoken=refreshtoken
          )
          data.save()
          return JsonResponse({'success': 'Login Successfully!!!', 'tokencreate':'token created successfully', 'accesstoken':accesstoken,'refreshtoken':refreshtoken},status=200)
        else:
          return JsonResponse({'error': 'password invalid.'},status=400)
