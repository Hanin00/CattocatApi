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
            if Cuser.objects.filter(email=data['email']).exists():
                user = Cuser.objects.get(email=data['email'])

                if bcrypt.checkpw(data['upassword'].encode("UTF-8"), user.upassword.encode('UTF-8')):
                    token = jwt.encode({'uid': user.uid}, SECRET_KEY, algorithm='HS256')
                   # token = jwt.encode({'uid': user.uid}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
                    return JsonResponse({'message': "SUCCESS", "token": token}, status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=400)

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
                upassword=bcrypt.hashpw(data["upassword"].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")
            ).save()

            return JsonResponse({'message': "SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)
