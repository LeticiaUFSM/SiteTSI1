from django.db import models

# Create your models here.

class Forum(models.Model):
	topico = models.CharField(max_length=100)
	descricao = models.TextField()
	
	def __str__(self):
		return self.topico

class Mensagem(models.Model):
    idforum = models.ForeignKey(Forum)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.mensagem

