from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def  register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        return render(request,"login.html")
    else:

        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        return redirect("/form")
    return render(request,"login.html")




def form(request):
    return render(request,"form.html")
def branches(request):

    return render(request,"branches.html")
def branch1(request):
    return render(request,"branch1.html")
def branch2(request):
    return render(request,"branch2.html")
def branch3(request):
    return render(request,"branch3.html")
def branch4(request):
    return render(request,"branch4.html")
def home(request):
    return render(request,"home.html")