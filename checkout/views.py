from django.shortcuts import render

# Create your views here.
def delivery(request):
    return render(request, 'home.html')