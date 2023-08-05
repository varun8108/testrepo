from django.shortcuts import render
from P1 import settings
from app1.models import Details
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        fathername = request.POST.get('fathername','')
        Class = request.POST.get('class','')
        age = request.POST.get('age',0)
        for file in dict(request.FILES)['file']:
            image = FileSystemStorage(location=settings.STATICFILES_DIRS[0]).save(file.name,file)
        
        obj = Details()
        obj.name = name
        obj.fathername = fathername
        obj.Class = Class
        obj.age = age
        obj.image = image
        obj.save()
        
        
        return render(request,'home.html',{'msg':'Done!!!'})
    return render(request,'home.html')

def Alldata(request):
    data = Details.objects.all()
    return render(request,'Alldata.html',{'data':data})
    

def single(request,id):
    data = Details.objects.first()
    return render(request,'single.html',{'data':data})