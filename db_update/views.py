from django.shortcuts import render
from db_insert import models
# Create your views here.
def home(request):
    return render(request,'update.html')

def dbupdate(request):
    id_front=request.GET['id']
    usn_front=request.GET['usn']
    s=models.Students.objects.get(id=id_front)
    s.usn=usn_front
    s.save()
    return render(request,'result.html')