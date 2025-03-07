from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Szemely

def fooldal(request):

    szemelyek = Szemely.objects.all()

    return render(request,'fooldal.html', {"szemelyek": szemelyek})

def rolunk(request):
    return render(request,'rolunk.html')

def uj_szemely(request):
 
    if request.method == "GET":
        return render(request,'uj_szemely.html')
    
    elif request.method == "POST":
        veznev = request.POST.get('veznev')
        kernev = request.POST.get('kernev')
        kor = request.POST.get('kor')
        hazas = request.POST.get('hazas')
        tortenet = request.POST.get('tortenet')

        if hazas == "on":
            hazas = True
        else:
            hazas = False

        szemely = Szemely(vezeteknev=veznev, keresztnev=kernev, eletkor=kor, hazas=hazas, elettortenet=tortenet)
        szemely.save()

        return redirect('fooldal')