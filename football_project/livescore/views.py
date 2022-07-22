from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import teamform
from .models import football

def new(request):
    teams=football.objects.all()
    context={
        'champions_list':teams
    }
    return render(request,'index.html',context)

def details(request,id):
    teams=football.objects.get(id=id)
    return render(request,'details.html',{'team':teams})
def add_team(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        disc=request.POST.get('disc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        team=football(name=name,disc=disc,year=year,img=img)
        team.save()
    return render(request,'add.html')
def update(request,id):
    team=football.objects.get(id=id)
    form=teamform(request.POST or None,request.FILES,instance=team)
    if form.is_valid():
        form.save()
        return redirect ('/')
    return render(request,'edit.html',{'form':form,'team':team})
def delete(request,id):
    if request.method=='POST':
        team=football.objects.get(id=id)
        team.delete()
        return redirect('/')
    return render(request,'delete.html')
