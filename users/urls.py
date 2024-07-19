from django.urls import path
from .views import logIniew, logOutView, signUpView

app_name = 'users'


urlpatterns = [
    path('signin/', logIniew, name='login'),
    path('signout/', logOutView, name='logout'),
    path('signup/', signUpView, name='signup'),
    
]
