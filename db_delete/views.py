from django.shortcuts import render
from db_insert import models
# Create your views here.
def home(request):
   return render(request,'delete.html')


def dbdelete(request):
    id_front=request.GET['id']
    models.Students.objects.get(id=id_front).delete()
    return render(request,'result.html')
    
