from django.db import models


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=45)
    cat_eye = models.CharField(max_length=45, blank=True, null=True)
    cat_hair = models.IntegerField(blank=True, null=True)
    cat_socks = models.IntegerField(blank=True, null=True)
    cat_locate = models.CharField(max_length=45, blank=True, null=True)
    cat_mom = models.IntegerField(blank=True, null=True)
    cat_tnr = models.IntegerField(blank=True, null=True)
    cat_prefer = models.CharField(max_length=200, blank=True, null=True)
    cat_special = models.CharField(max_length=200, blank=True, null=True)
    cat_similar = models.IntegerField(blank=True, null=True)
    cat_prof_img = models.CharField(max_length=200, blank=True, null=True)
    cat_image = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat'


# class CatsCat(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cat_name = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'cats_cat'


class Catuser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    user_phone = models.CharField(max_length=45, blank=True, null=True)
    user_image = models.CharField(max_length=45, blank=True, null=True)
    user_state = models.CharField(max_length=45, blank=True, null=True)
    user_city = models.CharField(max_length=45, blank=True, null=True)
    popup = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catuser'


class Userfollowcat(models.Model):
    pair_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Catuser, models.DO_NOTHING, blank=True, null=True)
    cat = models.ForeignKey(Cat, models.DO_NOTHING, blank=True, null=True)
    cat_name = models.CharField(max_length=45, blank=True, null=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userfollowcat'

