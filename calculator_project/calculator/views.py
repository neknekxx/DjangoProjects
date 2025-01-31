from django.shortcuts import render

def home(request):
    return render(request, 'calculator/home.html')  # Make sure this path matches the folder structure
