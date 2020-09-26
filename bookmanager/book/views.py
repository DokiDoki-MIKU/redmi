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
