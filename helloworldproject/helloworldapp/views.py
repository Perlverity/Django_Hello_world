from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hellofunction(request):
    return render(request, 'helloworldapp/hello.html')
