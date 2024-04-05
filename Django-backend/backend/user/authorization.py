from rest_framework.decorators import api_view
import jwt
from django.conf import settings
from django.http import JsonResponse
from .models import User
from django.contrib.auth.hashers import check_password
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)

        token = auth_header.split(' ')[1]
        try:
            decoded_token = jwt.decode(token, settings.ASECRET_KEY, algorithms=['HS256'])
            email = decoded_token.get('email')
            password = decoded_token.get('password')
            user = User.objects.get(email=email)
            if user and check_password(password, user.password):
                request.user = user
                return f(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=401)

    return decorated
# def token_required(f):
#     @wraps(f)
#     def decorated(request, *args, **kwargs):
#      auth_header = request.META.get('HTTP_AUTHORIZATION', '')
#      print(auth_header)
#      if auth_header.startswith('Bearer '):
#      token= auth_header.split(' ')[1]
#   try:
#         # Decode the JWT token using the secret key configured in Django settings
#         decoded_token = jwt.decode(token, settings.ASECRET_KEY, algorithms=['HS256'])
#         email=decoded_token.get('email',None)
#         password=decoded_token.get('password',None)
#         user=User.objects.get(email=email)
#         if check_password(user.password,password) :
#           return True
#         return False
#   except jwt.ExpiredSignatureError:
#         # Handle token expiration error
#         return JsonResponse({'error': 'Token has expired'})
#   except jwt.InvalidTokenError:
#         # Handle invalid token error
#         return JsonResponse({'error': 'Invalid token'})
#  return JsonResponse(None)