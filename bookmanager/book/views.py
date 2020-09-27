from django.shortcuts import render,redirect
from django.http import  HttpResponse
from book.models import BookInfo



def create_book(request):
   books=BookInfo.objects.create(
      name='adc',
      pub_date='2020-1-1',
      readcount=10

   )


   return HttpResponse('create')

###############增加############

def shop(request,city_id,mobile):
   print(city_id,mobile)

   query_params=request.GET
   print(query_params)
   oredr=query_params.getlist('order')
   print(oredr)
   return HttpResponse('古中国')

def register(request):
   data=request.POST
   print(data)
   return HttpResponse('ok')

def json(request):
   body=request.body
   body_str=body.decode()

   import json
   body_dict=json.load(body_str)

   print(request.META['SERVER_PORT'])
   return HttpResponse('json')

def method(request):
   print(request.method)
   return HttpResponse('method')

from django.http import  HttpResponse,JsonResponse
def response(request):
   info={
      'name':'itcast',
      'address':'shunyi'
   }
   girl_friends=[
      {
         'name':'rose',
         'address':'shuyi'
      },

      {'name':'rose',
       'address':'shunyi'

      }
   ]

   return redirect('www.baidu.com')



def set_cookie(request):
   username =request.GET.get("username")
   response = HttpResponse('set_cookie')
   response.set_cookie('name',username)
   return response
def get_cookie(requset):
   return HttpResponse('get_cookie')

def response(request):
   return HttpResponse('itcast python',statu=400)







































































































































































