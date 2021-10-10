from django.db import models
from django.conf import settings


class Cuser(models.Model):
    uid = models.AutoField(primary_key=True)
    #  uname = models.OneToOneField((User, related_name='profile', unique=True)
  #  uname = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cuser'
