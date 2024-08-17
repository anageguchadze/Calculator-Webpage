from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_view(request):
    return render(request, 'index.html')

def calculate_view(request, operation, num1, num2):
    num1, num2 = int(num1, num2)
    if operation == 'add':
        return HttpResponse(num1 + num2)
    elif operation == 'subtract':
        return HttpResponse(num1 - num2)
    elif operation == 'multiply':
        return HttpResponse(num1 * num2)
    elif operation == 'divide':
        return HttpResponse(num1 / num2)