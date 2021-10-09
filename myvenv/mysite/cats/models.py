from django.db import models


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=45)
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
    cat_xlocation = models.BigIntegerField(blank=True, null=True)
    cat_ylocation = models.BigIntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat'




class Cuser(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(unique=True, max_length=45)
    email = models.CharField(unique=True, max_length=45)
    upassword = models.CharField(max_length=45)
    phone = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    is_superuser = models.IntegerField()
    is_staff = models.IntegerField()
    popup = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuser'



class Pair(models.Model):
    pair_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Cuser, models.DO_NOTHING)
    cat = models.ForeignKey(Cat, models.DO_NOTHING)
    is_active = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=False)
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
    create_at = models.DateTimeField(blank=True, null=False)
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
    is_active = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=False)
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
    is_active = models.IntegerField()
    create_at = models.DateTimeField(blank=True, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reply'
