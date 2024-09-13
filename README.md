# Task Manager

O **Task Manager** é um projeto de gerenciamento de tarefas desenvolvido em Django, que permite que os usuários registrem, editem, filtrem, e excluam tarefas de maneira simples e eficiente. O projeto inclui funcionalidades de autenticação e registro de usuários, garantindo que cada usuário tenha acesso apenas às suas próprias tarefas.

## Funcionalidades

- **Cadastro de Usuários:** Os usuários podem se cadastrar na plataforma com um nome de usuário, e-mail e senha.
- **Login:** Sistema de autenticação de usuários com suporte para login seguro.
- **Logout:** Os usuários podem sair da plataforma com segurança.
- **Dashboard** Pagina de consulta de todas as tarefas do sistema com filtros por status.
- **lista de Tarefas:** Exibição de todas as tarefas do usuário, com opções para criar, editar, excluir e filtrar tarefas.
- **Gerenciamento de Tarefas:**
  - Criar novas tarefas com título, descrição, status e a atribuição.
  - Editar e atualizar tarefas existentes.
  - Excluir tarefas indesejadas.
- **Filtro de Tarefas por Status:** Os usuários podem filtrar as tarefas com base no status (como "Pendente", "Em Progresso", "Concluído", ou ver todas).

## Tecnologias Utilizadas

- **Django:** Framework de desenvolvimento web em Python, utilizado para construir o backend do projeto.
- **HTML/CSS:** Utilizados para o frontend, proporcionando uma interface de usuário simples e funcional.
- **SQLite:** Banco de dados padrão utilizado pelo Django para armazenamento de dados, mas pode ser substituído por outros sistemas de gerenciamento de banco de dados (MySQL, PostgreSQL, etc.).

## Estrutura do Projeto

TaskManager-Django/
│
├── autenticacao/              # Diretório principal do projeto Django
│   ├── __pycache__/           # Cache dos arquivos Python compilados
│   ├── __init__.py            # Indica que o diretório é um módulo Python
│   ├── asgi.py                # Configuração para o servidor ASGI
│   ├── settings.py            # Configurações do projeto Django
│   ├── urls.py                # Definições de URL do projeto
│   └── wsgi.py                # Configuração para o servidor WSGI
│
├── usuarios/                  # App de gerenciamento de usuários
│   ├── __pycache__/           # Cache dos arquivos Python compilados
│   ├── migrations/            # Diretório para arquivos de migração do Django
│   ├── static/                # Arquivos estáticos (CSS, JavaScript, imagens)
│   │   ├── css/               # Arquivos CSS
│   │   │   ├── style.css      # Estilos CSS personalizados
│   ├── templates/             # Templates HTML relacionados aos usuários
│   │   ├──cadastro.html       # Formulário de cadastro de usuários
│   │   ├──login.html          # Formulário de login de usuários
│   │   ├──dashboard.html      # Página principal do usuário
│   │   ├──task_confirm_delete.html # Página de confirmação de exclusão de tarefas
│   │   ├──task_form.html      # Formulário de criação e edição de tarefas
│   │   ├──task_list.html      # Lista de tarefas do usuário
│   ├── __init__.py            # Indica que o diretório é um módulo Python
│   ├── admin.py               # Configurações para a interface administrativa do Django
│   ├── apps.py                # Configurações do aplicativo Django
│   ├── forms.py               # Formulários utilizados no app de usuários
│   ├── models.py              # Definição dos modelos de dados
│   ├── tests.py               # Testes automatizados para o aplicativo (não aplicado)
│   ├── urls.py                # Definições de URL específicas para o app de usuários
│   └── views.py               # Lógica de controle para as views do app
│
├── .gitignore                 # Arquivos e pastas a serem ignorados pelo Git
├── db.sqlite3                 # Banco de dados SQLite padrão (pode variar)
└── manage.py                  # Utilitário de gerenciamento do Django
