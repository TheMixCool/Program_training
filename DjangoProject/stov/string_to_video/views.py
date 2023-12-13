from django.shortcuts import render

def string_to_video(request):
    return render(request, 'http://127.0.0.1:8001/', {})
    
def string_to_video(request):
    context = {'useful_value'}
    if request.method == "POST":
        string_to_video(useful_value, 1)
    return render(request, 'http://127.0.0.1:8001/', context)
