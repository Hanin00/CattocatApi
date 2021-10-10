from rest_framework import serializers
from .models import Cat, Cuser, Pair, Plike, Post, Reply
from rest_framework import serializers
from rest_framework.settings import api_settings
import time


'''
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']

        send_mail(
            '가입환영이메일',
            'Travel 블로그에 가입을 환영합니다!',
            'nldaseul@gmail.com',
            [user.email],
            fail_silently=False,
        )

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)

'''


class CattotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'


# user api
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['cat_id','cat_name', 'cat_eye', 'cat_hair', 'cat_socks', 'cat_locate', 'cat_mom', 'cat_tnr'
            , 'cat_prefer', 'cat_special', 'cat_similar', 'cat_prof_img', 'cat_image', 'cat_xlocation'
            , 'cat_ylocation', 'is_active']

    cat_id = serializers.IntegerField()
    cat_name = serializers.CharField(max_length=45)
    cat_eye = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    cat_hair = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    cat_socks = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    cat_locate = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    cat_mom = serializers.IntegerField()
    cat_tnr = serializers.IntegerField()
    cat_prefer = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    cat_special = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    cat_similar = serializers.IntegerField()
    cat_prof_img = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    cat_image = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    cat_xlocation = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)
    cat_ylocation = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)

  #  updated_at: str = serializers.DateTimeField(api_settings.DATETIME_FORMAT).to_representation(timestamp)

    is_active = serializers.IntegerField()




# Cuser - User 정보 변경

class CuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuser
        fields = ['uid','uname', 'email', 'phone',
                  'image', 'state', 'city', 'popup']

    uid = serializers.IntegerField()
    uname = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=45)
    phone = serializers.CharField(max_length=45)
    image = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    state = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    city = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    popup = serializers.IntegerField()


#  Pair - Pair 상태 변경 -> 고양이 follow
class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ['pair_id','user_id', 'user', 'cat', 'is_active']
        pair_id = serializers.IntegerField()
        user = serializers.IntegerField()
        cat = serializers.IntegerField()
        is_active = serializers.IntegerField()


#  Post - post 게시글 등록, 수정, 삭제, 불러오기
class PosttotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id','user', 'title', 'content', 'image', 'is_active']

        post_id = serializers.IntegerField()
        user = serializers.IntegerField()
        title = serializers.CharField(max_length=45)
        content = serializers.CharField()
        image = serializers.CharField(allow_blank=True, allow_null=True)
        is_active = serializers.IntegerField()


#  Plike - Plike 게시글 좋아요
class PlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plike
        fields = ['like_id','user', 'post', 'is_active']
        like_id = serializers.IntegerField()
        user = serializers.IntegerField()
        post = serializers.IntegerField()
        is_active = serializers.IntegerField()

#  Reply - 댓글
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['reply_id','user', 'post', 'content','is_active']

        reply_id = serializers.IntegerField()
        user = serializers.IntegerField()
        post = serializers.IntegerField()
        content = serializers.CharField()
        is_active = serializers.IntegerField()


#게시물 별 댓글 반환 필요