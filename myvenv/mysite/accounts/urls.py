from django.urls import path, include
from . import views
from .views import  CuserView, SignView

app_name = 'accounts'

urlpatterns=[
    path('', CuserView.as_view()),
    path('signup/',CuserView.as_view()),
    path('signin/', SignView.as_view()),
]