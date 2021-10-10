from django.urls import path, include
from . import views
from .views import  CuserView, SignUp,SignIn

app_name = 'accounts'

urlpatterns=[
    path('', CuserView.as_view()),
    path('signup/',SignUp.as_view()),
    path('signin/', SignIn.as_view()),
]