from django.urls import path, include
from . import views

app_name = 'cats'

urlpatterns=[
   # path('', views.cat_view, name = 'index'),
    path('totalcat/', views.cat_list),
    path('catdetail/<int:pk>/',views.cat_detail),

    path('totaluser/', views.cuser_list),
    path('userdetail/<int:pk>/', views.cuser_detail),

    path('totalpair/', views.pair_list),
    path('pairdetail/<int:pk>/', views.pair_detail),

    path('pair_modify_list/', views.pair_list),
    path('pair_modify_detail/<int:pk>/', views.pair_detail),

]