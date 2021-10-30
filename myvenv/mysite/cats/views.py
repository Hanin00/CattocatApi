from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .serializers import *
from .models import Cat,Cuser, Pair, Plike, Post, Reply, Pair, Notice, Info, CatImage
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
        mfilter = Pair.objects.filter(user_id=request.user.uid).values('cat_id').distinct()  # {"cat_id":1}, {"cat_id":2}
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
class CatTotalViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CattotalSerializer

cat_totallist = CatTotalViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


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


#설정 - 내가 좋아요한 글 목록
#user_id를 받아서 Plike.is_active=1인 값 추가
class userLikePostView(View):
#user_id에 따라 plike.is_active = 1인 post_id 출력
    def get(self, request):
        post_id = request.GET['user_id']
        pLikelist = Plike.objects.filter(user_id=user_id).values()
        return JsonResponse({'post_id': post_id, 'content': list(pLikelist)}, status=200)


class modifyLikePostView(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        pLikelist = Plike.objects.filter(like_id=data['like_id']).values()

        pLikelist.objects.update(
            uis_active=data['is_active'],
        )
        return JsonResponse({'content': list(pLikelist)}, status=200)




#user_id를 받아서 pLike.is_active=1인 값 추가


#  pLike
class ulikepostViewSet(ModelViewSet):
    queryset = Plike.objects.all()
    serializer_class = PlikeSerializer
# user 가 post id를 기준으로 plike is_active =1 한 테이블의 값 생성,수정
postulike = ulikepostViewSet.as_view({
    'post': 'create',
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




# post에 reply 등록, pli
class PidReplyView(View):
    def post(self, request):
        data = json.loads(request.body)
        # reply = Reply.objects.create()
        replylist = Reply.objects.create(user_id=data['user_id'], post_id=data['post_id']
                                        ,content=data['content']).values().count
        return JsonResponse({'post_id': post_id, 'content': list(replylist)}, status=200)

#pid로(포스팅별) 댓글 찾기
    def get(self, request):
        post_id = request.GET['post_id']
        replylist = Reply.objects.filter(post_id=post_id).values()
        return JsonResponse({'post_id': post_id, 'content': list(replylist)}, status=200)







#설정 - 내가 좋아요한 글 목록
#user_id를 받아서 Plike.is_active=1인 값 추가
class userLikePostView(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        #plike에 값 추가
        pLikecreate = Plike.objects.create(user_id=data['user_id'], post_id=data['post_id']).save()
        pLike_data = Plike.objects.filter(user_id=data['user_id'],post_id=data['post_id']).values()
        return JsonResponse({'post_id': post_id, 'content': list(pLike_data)}, status=200)

    # user_id를 받아서 pLike.is_active 수정
    def put(self, request):
        data = json.loads(request.body)
        pLikecreate = Plike.objects.update(user_id=data['user_id'], post_id=data['post_id'], is_active=data['is_active']).values()
        return JsonResponse({'post_id': post_id, 'content': list(pLikecreate)}, status=200)

#user_id에 따라 plike.is_active = 1인 post_id 출력
    def get(self, request):
        user_id = request.GET['user_id']
        pLikelist = Plike.objects.filter(user_id=user_id).values()
        return JsonResponse({'user_id': user_id, 'content': list(pLikelist)}, status=200)








#공지사항
class NoticeView(View):
    def get(self, request):
        noticelist = Notice.objects.values()
        return JsonResponse({'content': list(noticelist) }, status=200)

class NoticeContentView(View):
    def get(self, request):
        notice_id = request.GET['notice_id']
        noticecontent = Notice.objects.filter(notice_id=notice_id).values()
        return JsonResponse({'notice_id': notice_id, 'content': list(noticecontent)}, status=200)


#고양이 상식정보
class InfoView(View):
    def get(self, request):
        infolist = Info.objects.values()
        return JsonResponse({'content': list(infolist) }, status=200)

class InfoContentView(View):
    def get(self, request):
        info_id = request.GET['info_id']
        infocontent = Info.objects.filter(info_id=info_id).values()
        return JsonResponse({'info_id': info_id, 'content': list(infocontent)}, status=200)






#홈 화면에 필요한 것 - 하트 가장 많은 게시물, 공지사항 이미지와 링크 리스트,
class HomeView(View):
    def get(self, request):

        manylikepid = Plike.objects.all().values('post_id').annotate(total = Count('post_id')).order_by('-total')[:6]
        infolist = Info.objects.all().values().order_by('-created_at')[:6]
        noticelist = Notice.objects.all().values().order_by('-created_at')[:6]
        return JsonResponse({'bestpost': list(manylikepid), 'infolist': list(infolist), 'noticelist': list(noticelist)}, status=200)

#게시판 탭에 필요한 것 - 생성 순 게시글 data
class PostView(View):
    def get(self, request):
        postlist = Post.objects.all().values().order_by('-created_at') #user 와 join
        #userinfo = Cuser.objects.filter(uid=user_id).values('uname','city','image').values()
        return JsonResponse({'postlist': list(postlist)}, status=200)


#단일 게시글 조회 화면
class PostRpView(View):
    #리플 등록
    def post(self, request):
        data = json.loads(request.body)
        Reply.objects.create(user_id=data['user_id'], post_id=data['post_id'], content=data['content']).save()
        #    Reply.objects.create(user_id = request.user.uid, post_id = data['post_id'] , content = data['content']).save()

        return HttpResponse(status=200)

#게시글 내용과 댓글 불러오기.
    def get(self, request):
        post_id = request.GET['post_id']
        user_id = request.GET['user_id']
       # post = postu.objects.filter(post_id=post_id).values()
       # postu = Post.objects.extra(tables=['Cuser'], where=['Cuser.uid=Post.user_id']).values()
        postu = Post.objects.extra(tables=['Cuser'], where=['Cuser.uid=Post.user_id']).filter(post_id=post_id).values()
         #postu = Cuser.objects.extra(tables=['Post'], where=['Cuser.uid=Post.user_id']).values()


        userinfo = Cuser.objects.filter(uid=user_id).values()
        replylist = Reply.objects.filter(post_id=post_id).values()
        return JsonResponse({'post_id': post_id, 'post': list(postu), 'userinfo': list(userinfo), 'replylist': list(replylist)}, status=200)




# 고양이 등록 화면에 필요한 것 - 고양이 등록,














