from django.shortcuts import render
from main_management import views

# Create your views here.
def main(request) :
    return render(request, "main.html")
    
def history(request) :
    return render(request, "history.html")

def manager(request) :
    return render(request, "manager.html")