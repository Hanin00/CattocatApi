import datetime
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from accounts.views import Cuser


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    cat_name = models.CharField(max_length=45,null=False)
    cat_eye = models.CharField(max_length=45, blank=True, null=True)
    cat_hair = models.CharField(max_length=45, blank=True, null=True)
    cat_socks = models.CharField(max_length=45, blank=True, null=True)
    cat_locate = models.CharField(max_length=45, blank=True, null=True)
    cat_mom = models.IntegerField(default = 0)
    cat_tnr = models.IntegerField(default=0)
    cat_prefer = models.CharField(max_length=200, blank=True, null=True)
    cat_special = models.CharField(max_length=200, blank=True, null=True)
    cat_prof_img = models.CharField(max_length=200, blank=True, null=True)
    cat_image = models.CharField(max_length=200, blank=True, null=True)
    cat_xlocation = models.CharField(max_length=200, blank=True, null=True)
    cat_ylocation = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'Cat'





class Pair(models.Model):
    pair_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    cat_id = models.IntegerField()
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pair'




class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=45)
    content = models.TextField()
    image = models.TextField(blank=True, null=False)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Post'


class Plike(models.Model):
    like_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pLike'








#user 값 제외하면 단순히 id(Int) 값만 넣고 나중에 찾아서 보이면 됨
class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    #user = models.ForeignKey('Cuser', on_delete=models.CASCADE())
    post_id = models.IntegerField()
    content = models.TextField()
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reply'

