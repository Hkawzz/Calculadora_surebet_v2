from django.shortcuts import render

def inicio(request):
    return render(request, 'calculadora_2valores/index.html')