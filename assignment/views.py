from django.shortcuts import render


# Create your views here.

def assignment(request):
    return render(request, 'assignment.html')
