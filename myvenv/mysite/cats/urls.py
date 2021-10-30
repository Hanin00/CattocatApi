from django.urls import path, include
from django.views import View
from . import views
from .views import  *

app_name = 'cats'

urlpatterns=[
   # path('', views.cat_view, name = 'index')
    # cat

    path('totalcat/', views.cat_totallist),
    path('postcat/', views.cat_list),
    path('catdetail/<int:pk>/',views.cat_detail),

    # pair
    path('totalpair/', views.pair_list),
    path('pairdetail/<int:pk>/', views.pair_detail),

    # post
    # 게시글 작성 - / 가 붙으면  post 보내기 가능 없으면 단순 get
    path('posting/', views.post_list),   #등록시 sPref 의 user_id  보내기  #get시 모든 포스팅 / post 시 title, content만으로 작성 가능
    # 단일 게시글 수정,
    path('postdetail/<int:pk>/', views.post_detail),   #등록시 sPref 의 user_id  보내기

    # plike
    path('ulikepost/', userLikePostView.as_view()),   #user가 좋아한 글 목록 - get / user_id
    path('postulike/', views.postulike),   #post - user가 하트 누른거 추가
   # path('putulike/', views.postulike),    #put - user 하트 상태 변경 plike_id
    path('putulike/', modifyLikePostView.as_view()),    #put - user 하트 상태 변경 plike_id




    # Reply
    path('totalreply/', views.reply_list),  # get : 모든 댓글 / post : "user_id": "2","post_id": "3","content": "4시 되면 갈거야"
    path('replydetail/<int:pk>/', views.reply_detail), #get : reply_id 해당 댓글 가져오기, #put 해당 댓글 수정
    path('pidreply/', PidReplyView.as_view()), #get : post 별 댓글 가져오기, #post : post 별 댓글 달기





    #notice
    path('notice/', NoticeView.as_view()),  # get : 모든 공지사항
    path('noticecnt/', NoticeContentView.as_view()),  # get : notice_id  필터링해서 내용만 보냄

    # info
    path('info/', InfoView.as_view()),  # get : 모든 상식 정보
    path('infocnt/', InfoContentView.as_view()),  # get : info_id  필터링해서 내용만 보냄

#home
    path('home/', HomeView.as_view()),  # get : best 게시글
#board
    path('post/', PostView.as_view()),  # get : 전체 글 목록 + 해당 포스트에 맞는 userinfo
#singlepost
    path('postsingle/', PostRpView.as_view()),  #get : post, reply  내용, 리스트 불러옴, post : reply 전송











    #cat 등록 후 Pair로 연계 동작하게 구현할 것.
    #Deco 적용  pair,
    # Reply - deco
    path('reply/', ReplyView.as_view()), #get인 경우 : 모든 댓글 #post인 경우 등록 가능 "user_id","post_id","content"
    path('pair/', PairView.as_view()), #get인 경우 모든 pair 출력, post 인 경우 등록가능  "cat_id": 5,"user_id": 2
    path('mpair/', personalPairView.as_view()),  # get : user jwt에 맞는 cat_id 출력 {"cat_id":1}, {"cat_id":2} post의 경우 cat_id 전송하여 등록 가능
    path('ppair/', PerPariView.as_view()), # pair 정보  중복제거 X
    path('mycat/', MyCatView.as_view()), # post - uid가 같이 등록됨, get - uid에 맞는 고양이만 반환됨
    path('userinfo/', CuserInfoView.as_view()), #get  jwt로 userInfo 반환
    #user의 댓글 모으기

    #user 작성 포스팅

    #user가 만든 like - post_id -> 일단 XX join 해야함


    #cat 등록 시 cat_id return 으로 받아야함.

]


'''    # user
    path('totaluser/', views.cuser_list),
    path('muserdetail/<int:pk>/', views.cuser_detail),'''
