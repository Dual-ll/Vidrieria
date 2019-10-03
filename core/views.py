from django.shortcuts import render

def index(request):
    template = 'core/home.html'
    return render(request, template)
