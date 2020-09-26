from django.shortcuts import render
from django.http import  HttpResponse

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
from book.models import BookInfo
try:
   book=BookInfo.objects.get(id=3)

except BookInfo.DoesNotExist:
   print('查询结果不存在')

BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()

BookInfo.objects.all().count()
BookInfo.objects.count()

from django.db.models import F
BookInfo.objects.filter(readcount__gt=F('commentcount'))