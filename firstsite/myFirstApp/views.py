from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
import datetime
class MyClass:
    string = ""
    def __init__(self,s):
        self.string = s

def main(request):
    return render(request,'index.html',)

def first(request):
    return HttpResponse("Переход по ссылке")
def two(request,one):
    return HttpResponse(f"two{one}")

def test(request):
    return HttpResponse("Two but another")

def rectangle(request,one,two):
    return HttpResponse(f"area {one * two}")

def Name(request):
    user_name = "Бублик"
    return render(request, 'user.html', {'user_name':user_name})

def fun():
    try:
        comment = Comment.objects.get(article_genre_in=[2,3])
    except Comment.MultipleObjectReturned:
        return "More then object"
    except Comment.DoesNotExist:
        return "Cant find object"
def fun2():
    Comment.objects.all()
    Comment.objects.filter(text="Hey everyone")

def form_view (request):
    # return render(request,'form.html')
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request,'formValid.html')
    else:
        form = MyForm()
    return render(request,"form.html",{'form':form})

def my_login(request):
    if request.method == 'POST':
        form = AuthentificationForm(request.POST)
        if form.is_valid():
            login(request,form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthentificationForm()
    return render(request,'login.html',{'form':form})
@login_required(login_url='accaunt/login/')

def logout_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pass
        logout(request)


