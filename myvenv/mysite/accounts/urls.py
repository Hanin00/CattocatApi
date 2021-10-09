from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns=[
   # path('', views.cat_view, name = 'index'),
    path('', views.profile, name='profile'),
]