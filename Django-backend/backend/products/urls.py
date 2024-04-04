from django.urls import path
from .views import create,load,update,delete

urlpatterns = [
  path('create/',create,name='create'),
  path('load/',load,name='load'),
  path('update/<int:id>/',update,name='update'),
  path('delete/<int:id>/',delete,name='delete'),
]
