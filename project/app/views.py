from django.shortcuts import render
from django.http.response import HttpResponse
from frontend import views

# Create your views here.
def index(request):
    return render(request, 'frontend/templates/index.html')
    #return HttpResponse("test")

 
 
 
 


 
 