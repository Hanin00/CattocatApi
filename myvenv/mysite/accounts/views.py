from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from  .models import Cuser
from django.views import View
from django.http import HttpResponse,JsonResponse


class  CuserView(View):
    def post(self, request):
        data = json.loads(request.body)
        Cuser.objects.create(
            uid= data['uid'],
            uname= data['uname'],
            email= data['email'],
            upassword= data['upassword'],
            phone= data['phone']
        )
        
        return HttpResponse(status=200)
    
    def get(self, request):
        Cuser_data = Cuser.objects.values()
        return JsonResponse({'cusers' : list(Cuser_data)}, status=200)
    
    
class SignView(View) : 
    def post(self, request):
        data = json.loads(request.body)
        
        try : 
            if Cuser.objects.filter(email= data['email']).exists():
                user = Cuser.objects.get(email=data['email'])
                
                if user.password == data['password']:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=400)
        
        except KeyError :
            return JsonResponse({'message' : "INVALID_KEYS"}, status=400)
        
        