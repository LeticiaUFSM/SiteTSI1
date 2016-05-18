from django.db import models

# Create your models here.

class Noticias(models.Model):
    #atributos
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.titulo

class ImagensNoticia(models.Model):
    idnoticia = models.ForeignKey(Noticias)
    legenda = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.legenda
