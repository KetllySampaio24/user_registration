from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

# Página inicial
def home(request):
    return render(request, 'usuarios/home.html')

# Cadastro de novo usuário e exibição da lista
def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
    # Listagem após cadastro
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuarios/usuarios.html', usuarios)

# View para editar um usuário
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.idade = request.POST.get('idade')
        usuario.save()
        return redirect('listagem_usuarios')

    return render(request, 'usuarios/editar.html', {'usuario': usuario})

# View para excluir um usuário
def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)
    usuario.delete()
    return redirect('listagem_usuarios')
