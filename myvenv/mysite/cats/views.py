from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import CatSerializer, CatModifySerializer
from .models import Cat, Catuser, Userfollowcat


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
