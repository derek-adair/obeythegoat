from django.shortcuts import render

def home_page(request):
    return render('<html><title>To-Do lists</title></html>', 'home.html')
