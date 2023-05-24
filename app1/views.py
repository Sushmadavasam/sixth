from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>This is my first project</h1>')

def first1(request):
    return render(request,'first1.html')