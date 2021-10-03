from django.urls import path, include
from . import views

app_name = 'cats'

urlpatterns=[
   # path('', views.cat_view, name = 'index'),
    path('totalcat/', views.cat_list),
    path('catdetail/<int:pk>/',views.cat_detail),
]