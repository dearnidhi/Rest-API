import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_home(request, *args, **kwargs):
    body =request.body
    data = {}
    try: 
        data = json.loads(body)
    except:
        pass    
    print(data.keys())
    return JsonResponse({"message":"Hi i am nidhi ,i am learning coding with you and thi is your api response"})


