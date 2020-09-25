from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def index(request):
    context = {'title':'测试模板数据'}
    return render(request,'book/index.html',context)