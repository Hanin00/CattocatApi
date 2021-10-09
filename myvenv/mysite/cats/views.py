from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import *
from .models import Cat, Cuser, Pair, Plike, Post, Reply, Pair
from rest_framework import generics


def cat_view(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})


class CatViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


cat_list = CatViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

cat_detail = CatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class CatModifyViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatModifySerializer


cat_mlist = CatModifyViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

cat_detail = CatModifyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


#  Cuser - User 상태 변경
def Cuser_view(request):
    cuser = Cuser.objects.all()
    return render(request, 'index.html', {'cuser': cuser})


class CuserViewSet(ModelViewSet):
    queryset = Cuser.objects.all()
    serializer_class = CuserModifySerializer


cuser_list = CuserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
cuser_detail = CuserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


#  Pair - Pair 상태 변경
def Pair_view(request):
    pair = Pair.objects.all()
    return render(request, 'index.html', {'pair': pair})


class PairViewSet(ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer


pair_list = PairViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

pair_detail = PairViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


class PairModifyViewSet(ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = PairModifySerializer


mpair_list = PairModifyViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


#put으로 수정작업
mpair_detail = PairModifyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

