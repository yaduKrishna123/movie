
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .models import movie
from .forms import MovieForm


# Create your views here.
def demo(request):
    Movie=movie.objects.all()
    context={'movielist':Movie}
    return render(request,'index.html',context)
def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'Movie':Movie})
def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dec=request.POST.get('dec')
        year=request.POST.get('year')
        img=request.FILES['img']
        Movie=movie(name=name,dec=dec,year=year,img=img)
        Movie.save()
    return render(request,'add.html')
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Movie':Movie})
def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')

