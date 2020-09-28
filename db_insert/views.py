from django.shortcuts import render
from db_insert import models
# Create your views here.

def home(request):
    return render(request,'home.html')

def insert(request):
    name=request.GET['name']
    usn=request.GET['usn']
    s=models.Students()
    s.name=name
    s.usn=usn
    s.save()
    return render(request,"result.html")