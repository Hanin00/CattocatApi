from rest_framework import serializers
from .models import Cat,Catuser,Userfollowcat

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'


class CatModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['cat_name', 'cat_locate', ]

    cat_name = serializers.CharField(max_length=45)
    cat_locate = serializers.CharField(max_length=80)
