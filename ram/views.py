from django.shortcuts import render,redirect
from .models import indore


def create(request):
    data=indore.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        gmail=request.POST['gmail']
        passw=request.POST['passw']
        mobile=request.POST['mobile']
        date=request.POST['date']
        data=indore(name=name,gmail=gmail,passw=passw,mobile=mobile,date=date).save()
        data=indore.objects.all()
        return render(request,'ram/create.html',{'key':data})
    return render(request,'ram/create.html',{'key':data})

def update(request):
    data=indore.objects.get(pk=request.GET['pravin'])
    if request.method=='POST':
        data.name=request.POST['name']
        data.gmail=request.POST['gmail']
        data.passw=request.POST['passw']
        data.mobile=request.POST['mobile']
        data.date=request.POST['date']
        data.save()
        return redirect('/')
    return render(request,'ram/update.html',{'key1':data})
def delete(request):
    data=indore.objects.get(pk=request.GET['q']).delete()
    return redirect('/')

# Create your views here.
