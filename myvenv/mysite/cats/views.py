from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .serializers import *
from .models import Cat,Cuser, Pair, Plike, Post, Reply, Pair
from rest_framework import generics


import json
from accounts.views import LoginConfirm

# 로그인 데코레이터 적용v

# Cuser
class CuserInfoView(View):
    @LoginConfirm #get시 userId인 것만 모두 리턴(내 고양이)
    def get(self, request):
        userinfo_data = Cuser.objects.filter(uid=request.user.uid).values()
        return JsonResponse({'content': list(userinfo_data)}, status=200)



# Reply
class ReplyView(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        Reply.objects.create(user_id=request.user.uid, post_id=data['post_id'], content=data['content']).save()
        #    Reply.objects.create(user_id = request.user.uid, post_id = data['post_id'] , content = data['content']).save()

        return HttpResponse(status=200)

    def get(self, request):
        reply_data = Reply.objects.values()
        return JsonResponse({'content': list(reply_data)}, status=200)


# Pair
class PairView(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        Pair.objects.create(user_id=request.user.uid, cat_id=data['cat_id']).save()
        return HttpResponse(status=200)

    def get(self, request):
        pair_data = Pair.objects.values()
        return JsonResponse({'content': list(pair_data)}, status=200)


# Pair - 고양이 번호만 출력
class personalPairView(View):
    @LoginConfirm
    def get(self, request):
        # follow 하는 고양이 id만 list로 출력
        # mfilter = Pair.objects.filter(user_id=request.user.uid).values_list('cat_id',flat=True).distinct()  # -> list로 받음 [2,1,3]
        mfilter = Pair.objects.filtefr(user_id=request.user.uid).values('cat_id').distinct()  # {"cat_id":1}, {"cat_id":2}
        return JsonResponse({'content': list(mfilter)}, status=200)

    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        Pair.objects.create(user_id=request.user.uid, cat_id=data['cat_id']).save()
        return HttpResponse(status=200)

# cat_id  중복제거 X
class PerPariView(View):
    @LoginConfirm
    def post(self, request):
        pair_data = Pair.objects.filter(user_id=request.user.uid)
        pair = Pair.objects.filter(pair_id__in=pair_data).distinct().order_by('-create_at').values()

        return JsonResponse({'content': list(pair)}, status=200)


class MyCatView(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        Cat.objects.create(
            user_id=request.user.uid,
            #user_id=data['user_id'],
            cat_name=data['cat_name'],
            cat_eye=data['cat_eye'],
            cat_hair=data['cat_hair'],
            cat_socks=data['cat_socks'],
            cat_locate=data['cat_locate'],
            cat_mom=data['cat_mom'],
            cat_tnr=data['cat_tnr'],
            cat_prefer=data['cat_prefer'],
            cat_special=data['cat_special'],
            cat_prof_img=data['cat_prof_img'],
            cat_image=data['cat_image'],
            cat_xlocation=data['cat_xlocation'],
            cat_ylocation=data['cat_ylocation'],
        )

        return JsonResponse({'user_id': request.user.uid }, status=200)


    @LoginConfirm #get시 userId인 것만 모두 리턴(내 고양이) 
    def get(self, request):
        Cat_data = Cat.objects.filter(user_id=request.user.uid).values()
        return JsonResponse({'content': list(Cat_data)}, status=200)




# 로그인 데코레이터 적용 X v
#모든 Cat 조회, 중복 제거 후 marker 찍을 때 써야함
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


#  Pair - Pair 상태 변경
class PairViewSet(ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer



pair_list = PairViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# put으로 수정작업
pair_detail = PairViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})



#  Post - post 상태 변경
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# put으로 수정작업
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})



# todo counting
#  Plike - plike 좋아요
class PlikeViewSet(ModelViewSet):
    queryset = Plike.objects.all()
    serializer_class = PlikeSerializer


plike_list = PlikeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# put으로 수정작업
plike_detail = PlikeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})


#  Reply - Reply
class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


reply_list = ReplyViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# put으로 수정작업
reply_detail = ReplyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})
