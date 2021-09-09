from django.http import HttpResponse
from django.shortcuts import render

# Function will return to client
def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return HttpResponse('About page')
