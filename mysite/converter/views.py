from django.shortcuts import render
from django.http import FileResponse
from .models import MyClass
from foo import string_to_video


def page(request):
    text = request.GET.get('text')
    speed = request.GET.get('speed')
    
    MyClass.objects.create(
    	request = request.GET.get('text')
        
    )
    speed = 1
    string_to_video(text, speed)
    
    return render(request,'index.html')
