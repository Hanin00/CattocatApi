from django.urls import path, include
from django.views import View
from . import views
from .views import  ReplyView

app_name = 'cats'

urlpatterns=[
   # path('', views.cat_view, name = 'index')
    # cat
    path('totalcat/', views.cat_list),
    path('catdetail/<int:pk>/',views.cat_detail),

    # pair
    path('totalpair/', views.pair_list),
    path('pairdetail/<int:pk>/', views.pair_detail),

    # post
    path('totalpost/', views.post_tlist),
    # 게시글 작성 - / 가 붙으면  post 보내기 가능 없으면 단순 get
    path('posting/', views.post_list),
    # 단일 게시글 수정,
    path('postdetail/<int:pk>/', views.post_detail),
    # PostId 반환,
    path('tpostdetail/<int:pk>/', views.post_tdetail),

    # plike
    path('totalplike/', views.plike_list),
    path('plikedetail/<int:pk>/', views.plike_detail),

    # Reply
    path('totalreply/', views.reply_list),
    path('replydetail/<int:pk>/', views.reply_detail),

    #cat 등록 후 Pair로 연계 동작하게 구현할 것.
    #Deco 적용  pair,
    # Reply - deco
    path('reply/', ReplyView.as_view()),

]


'''    # user
    path('totaluser/', views.cuser_list),
    path('muserdetail/<int:pk>/', views.cuser_detail),'''
