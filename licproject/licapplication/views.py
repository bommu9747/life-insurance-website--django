from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def headoffice(request):
    return render(request,'headoffice.html')
def login(request):
    return render(request,'login.html')