from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def hello_blog(request):
    list_posts = Post.objects.all()
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de dados', 'Linux']
    data = {'name': 'Curso de Django 3', 'lista_tecnologias': lista, 'posts': list_posts }

    #return HttpResponse("Blog")
    
    return render(request, 'index.html', data)