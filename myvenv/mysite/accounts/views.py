from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cuser
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
import bcrypt
import jwt
from .models import Cuser
from mysite.settings import SECRET_KEY


class CuserView(View):
    def post(self, request):
        data = json.loads(request.body)
        Cuser.objects.create(
            uid=data['uid'],
            uname=data['uname'],
            email=data['email'],
            upassword=data['upassword'],
            phone=data['phone']
        )

        return HttpResponse(status=200)

    def get(self, request):
        Cuser_data = Cuser.objects.values()
        return JsonResponse({'cusers': list(Cuser_data)}, status=200)


class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Cuser.objects.filter(email=data["email"]).exists():
                user = Cuser.objects.get(email=data["email"])

                if bcrypt.checkpw(data['upassword'].encode('UTF-8'), user.upassword.encode('UTF-8')):
                    token = jwt.encode({'uid': user.uid}, SECRET_KEY, algorithm='HS256')

                    return JsonResponse({"uid":user.uid,"token" : token}, status=200)

                return JsonResponse({'message': "PASSWORD_ERROR"}, status=401)

            return JsonResponse({'message': "NOT_EXIST"}, status=402)

        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)


class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Cuser.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': "EXISTS_EMAIL"}, status=400)

            Cuser.objects.create(
                email=data['email'],
                upassword=bcrypt.hashpw(data["upassword"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            ).save()

            return JsonResponse({'message': "SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)





#인증 데코레이터 class
class LoginConfirm :
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, request, *args, **kwargs):
        token =  request.headers.get("JWTtoken", None)
        try :
            if token :
                token_payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                user = Cuser.objects.get(uid=token_payload['uid'])
                request.user = user
                return self.original_function(self, request, *args, **kwargs)
            return JsonResponse({'message':'NEED_LOGIN'},status=401)
        except jwt.ExpiredSignatureError :
            return JsonResponse({'message': 'EXPIRED_TOKEN'},status=401)

        except jwt.DecodeError :
            return JsonResponse({'message': 'INVALID_USER'},status=401)

        except Cuser.DoesNotExist :
            return JsonResponse({'message': 'INVALID_USER'},status=401)

