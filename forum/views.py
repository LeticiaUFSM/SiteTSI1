from django.shortcuts import render

from django.http import HttpResponse
from .models import Forum
from .models import Mensagem

#################################
# Importa form
from .forms import FormMensagem

# Create your views here.

def index(request):
    foruns = Forum.objects.all() 
    return render(request,'listaforuns.html',{'foruns':foruns})

def lermensagens(request, id):
	forum = Forum.objects.get(id=id) 
	mensagens = Mensagem.objects.all().filter(idforum=id)
	return render(request,'lermensagens.html',{'forum':forum, 'mensagens':mensagens})
	
def escrevermensagem(request, id, msg_id=None):
	if msg_id:
		mensagem = Mensagem.objects.get(id=msg_id)
	else:
		mensagem = None
        
	forum = Forum.objects.get(id=id)
	
	if request.method == 'POST':
		form = FormMensagem(request.POST, instance=mensagem)

	# Cria form
	#form = FormMensagem(request.POST)
	# Valida e salva
		if form.is_valid():
			msg = form.save(commit=False)
			msg.idforum = forum
			#msg.data = timezone.now()
			msg.save()
			return HttpResponse("Dados inseridos com sucesso!")
	# Chama Template
	else:
		form = FormMensagem(instance=mensagem)
    
	return render(request, 'escrevermensagem.html', {'form': form})

