from django.shortcuts import render

# Create your views here.

def chicago(request):

  return render(request, 'main/index.html')