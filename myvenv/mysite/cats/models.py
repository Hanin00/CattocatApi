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
    cat_name = models.CharField(max_length=45,null=False)
    cat_eye = models.CharField(max_length=45, blank=True, null=True)
    cat_hair = models.CharField(max_length=45, blank=True, null=True)
    cat_socks = models.CharField(max_length=45, blank=True, null=True)
    cat_locate = models.CharField(max_length=45, blank=True, null=True)
    cat_mom = models.IntegerField(blank=True, null=True)
    cat_tnr = models.IntegerField(blank=True, null=True)
    cat_prefer = models.CharField(max_length=200, blank=True, null=True)
    cat_special = models.CharField(max_length=200, blank=True, null=True)
    cat_similar = models.IntegerField(blank=True, null=True)
    cat_prof_img = models.CharField(max_length=200, blank=True, null=True)
    cat_image = models.CharField(max_length=200, blank=True, null=True)
    cat_xlocation = models.CharField(max_length=200, blank=True, null=True)
    cat_ylocation = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'cat'





class Pair(models.Model):
    pair_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Cuser, models.DO_NOTHING)
    cat = models.ForeignKey(Cat, models.DO_NOTHING)
    is_active = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pair'



class Plike(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Cuser, models.DO_NOTHING)
    post = models.ForeignKey('Post', models.DO_NOTHING)
    is_active = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plike'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Cuser, models.DO_NOTHING)
    title = models.CharField(max_length=45)
    content = models.TextField()
    image = models.TextField(blank=True, null=False)
    is_active = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Cuser, models.DO_NOTHING)
    post = models.ForeignKey(Post, models.DO_NOTHING)
    content = models.TextField()
    is_active = models.IntegerField(default=1)
    create_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reply'
