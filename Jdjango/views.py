from django.shortcuts import HttpResponse
def home(request):
    return HttpResponse("This is my Home page")
def contact(request):
    return HttpResponse("Do you find a python developer?Then contact with me")
def aboutme(request):
    return HttpResponse("this is my about me page")
def service(request):
    return HttpResponse("services are unavailable now!")
def info(request,name,age):
    return HttpResponse("welcome {}.your age is {} years old".format(name,age))
    
