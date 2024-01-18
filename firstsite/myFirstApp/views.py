from django.shortcuts import render
from django.http import HttpResponse
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



