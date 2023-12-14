from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de dados', 'Linux']
    data = {'name': 'Curso de Django 3', 'lista_tecnologias':lista}

    #return HttpResponse("Blog")
    return render(request, 'index.html', data)