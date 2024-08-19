from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_view(request):
    return render(request, 'index.html')

def calculate_view(request, operation, a, b):
    if operation == 'add':
        return HttpResponse(a + b)
    elif operation == 'subtract':
        return HttpResponse(a - b)
    elif operation == 'multiply':
        return HttpResponse(a * b)
    elif operation == 'divide':
        return HttpResponse(a / b)