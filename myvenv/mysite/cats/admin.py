from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Cat)
admin.site.register(Catuser)
admin.site.register(Userfollowcat)