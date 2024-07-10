from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<span>Info about us</<span>")

def contact(request):
    return HttpResponse("<h3>To stay in contact with us, you should email to balaniouk@gmail.com</h3>")