from django.shortcuts import render
from db_insert import models
# Create your views here.
def home(request):
    return render(request,'select.html')


def dbselect(request):
    id_front=request.GET['id']
    data=models.Students.objects.get(id=id_front)
    return render(request,'select_result.html',{'data':data})
