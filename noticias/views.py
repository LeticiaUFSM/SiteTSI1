from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticias
from .models import ImagensNoticia

# Create your views here.

def index(request):
    noticias = Noticias.objects.all() #recupera todas as noticias cadastradas
    return render(request,'listanoticias.html',{'noticias':noticias})

def lernoticia(request, id):
	noticia = Noticias.objects.get(id=id) #recupera apenas a noticia com o id recebido
	imagens = ImagensNoticia.objects.all().filter(idnoticia=id)
	return render(request,'detalhenoticia.html',{'noticia':noticia, 'imagens':imagens})
