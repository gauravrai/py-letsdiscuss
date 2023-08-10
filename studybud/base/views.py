from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Hey there')

def rooms(request):
    return HttpResponse('Rooms here')