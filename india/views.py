from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ind(request):
    return render(request,"india.html")
def ind1(request):
    return HttpResponse("hi i am india")