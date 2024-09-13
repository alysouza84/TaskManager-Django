from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
from django.contrib import messages
from .models import Task
from .forms import TaskForm, TaskFilterForm



#Função de cadastro
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('password')

            # Verifica se todos os campos foram preenchidos
            if not username or not email or not senha:
                messages.error(request, 'Preencha todos os campos')
                return render(request, 'cadastro.html')
            
            # Verifica se o usuário já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe')
                return render(request, 'cadastro.html')

            # Tenta criar um novo usuário
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()

            return redirect('login')

        except Exception as e:
            # Captura qualquer exceção e exibe uma mensagem de erro
            messages.error(request, f'Ocorreu um erro: {str(e)}')
            return render(request, 'cadastro.html')    

#Função de login    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Verifica se todos os campos foram preenchidos
            if not username or not password:
                messages.error(request, 'Preencha todos os campos')
                return render(request, 'login.html')
            
            # Autentica o usuário
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login_django(request, user)
                return redirect('task_list')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('login')

        except Exception as e:
            # Captura qualquer exceção e exibe uma mensagem de erro
            messages.error(request, f'Ocorreu um erro: {str(e)}')
            return render(request, 'login.html')

#lista de tarefas
@login_required
def task_list(request):
    form = TaskFilterForm(request.GET) # Cria um formulário de filtro
    tasks = Task.objects.filter(user=request.user) # Filtra as tarefas do usuário logado
    
    if form.is_valid():
        status = form.cleaned_data.get('status')
        if status:
            tasks = tasks.filter(status=status)
            
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form}) # task_list.html é a página de listagem de tarefas

#Criar tarefa
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) # Cria um formulário com os dados enviados pelo usuário
        if form.is_valid():
            task = form.save(commit=False) # Salva o formulário sem enviar ao banco de dados
            task.user = request.user # Adiciona o usuário logado à tarefa
            task.save() # Salva a tarefa no banco de dados
            messages.success(request, 'Tarefa criada com sucesso')
            return redirect('task_list') # Redireciona para a lista de tarefas
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form}) # task_form.html é a página de formulário

#Editar tarefa
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user) # Verifica se a tarefa pertence ao usuário logado
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form}) # task_form.html é a página de formulário

#Deletar tarefa
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user) # Verifica se a tarefa pertence ao usuário logado
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa deletada com sucesso')
        return redirect('task_list')
    return render(request, 'task_delete_confirm.html', {'task': task}) # task_delete_confirm.html é a página de confirmação de exclusão