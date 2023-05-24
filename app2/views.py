from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def second(request):
    return HttpResponse('<h1>This is my second project<h1> ')
def second2(request):
    return render(request,'second2.html')