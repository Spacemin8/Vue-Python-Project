from django.urls import path
from .views import create,load,update,delete

urlpatterns = [
  path('create/',create,name='create'),
  path('load/',load,name='load'),
  path('update/',update,name='update'),
  path('delete/',delete,name='delete'),
]
