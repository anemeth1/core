from django.shortcuts import render
from django.http import HttpResponse
from . models import szemely

def fooldal(request):

    szemelyek = szemely.objects.all()

    return render(request,'fooldal.html', {"szemelyek": szemelyek})

def rolunk(request):
    return render(request,'rolunk.html')