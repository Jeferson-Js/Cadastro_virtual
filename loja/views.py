from django.shortcuts import render, get_object_or_404, redirect
from .models import User

# Create your views here.
def loja(request):
    usuarios = User.objects.all()
    return render(request, 'loja/loja.html', {'usuarios': usuarios}) 

def create(request):
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        User.objects.create(nome=nome, idade=idade)
        usuarios = User.objects.all()
        return render(request, 'loja/loja.html', {"usuarios": usuarios})

def update(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        usuario.nome = nome
        usuario.idade = idade
        usuario.save()
        return redirect('loja')
    return render(request, 'loja/update.html', {'usuario': usuario})

def delete(request, id):
      usuario = get_object_or_404(User, id=id)
      usuario.delete()
      return redirect('loja')