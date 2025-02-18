from django.shortcuts import render
from .models import leiloeiro
from .models import matricula
from .models import estado

def home(request):
    return render(request,'cadastro/home.html')

def leiloeiros(request):
    novo_leiloeiro = leiloeiro()
    novo_leiloeiro.nome = request.POST.get('nome')
    novo_leiloeiro.cpf = request.POST.get('cpf')
    novo_leiloeiro.email = request.POST.get('email')
    novo_leiloeiro.telefone = request.POST.get('telefone')
    novo_leiloeiro.site = request.POST.get('site')
    novo_leiloeiro.matricula = request.POST.get('matricula')
    novo_leiloeiro.save()

    #exibir infos em nova tela.
    leiloeiro = {
        'leiloeiro': leiloeiro.objects.all()
    }
    return render(request,'leiloeiros/',leiloeiros)

