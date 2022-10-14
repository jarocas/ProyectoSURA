from django.shortcuts import render

# Create your views here.
#render (renderizar) es pintar
def Home(request):
    return render(request,'index.html')