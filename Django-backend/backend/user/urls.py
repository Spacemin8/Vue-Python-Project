from django.urls import path
from .views import signup
from .views import login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
