from rest_framework import serializers
from .models import Cat, Cuser, Pair, Plike, Post, Reply

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'


class CatModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['cat_name', 'cat_locate']

    cat_name = serializers.CharField(max_length=45)
    cat_locate = serializers.CharField(max_length=80)

#Cuser - User 정보 변경
class CuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuser
        fields = '__all__'

class CuserModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuser
        fields = ['uname', 'email','phone',
                  'image','state','city', 'popup']

    uname = serializers.CharField( max_length=45)
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
        fields = '__all__'

class PairModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ['user', 'cat', 'is_active']
        user = serializers.IntegerField()
        cat = serializers.IntegerField()
        is_active = serializers.IntegerField()
