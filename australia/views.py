from django.shortcuts import render

# Create your views here.
def aus1(request):
    return HttpResponse('hi i am australia')
def aus(request):
    return render(request,"australia.html")