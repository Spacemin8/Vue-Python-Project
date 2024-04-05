from django.urls import path
from .views import signup,verifycode,password_set,login
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/verify/', verifycode, name='verify'),
    path('signup/setpassword/', password_set, name='setpassword'),
    path('login/', login, name='login'),
]
