from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from book.models import BookInfo
def index(request):
   books=BookInfo.objects.all()
   print(books)

   return HttpResponse('index')

###############增加############
from book.models import BookInfo
book = BookInfo(
   name = 'Django',
   pub_date='2000-1-1',
   readcount=10
)
book.save()

BookInfo.objects.create(
   name='测试开发入门',
   pub_date='2020-1-1',
   readcount=100
)

