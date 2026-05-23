# 🚀 Flask Authentication System with Blueprints

## 📌 Visão Geral

Este projeto é uma aplicação web desenvolvida com Python utilizando o framework entity["software","Flask","Python web framework"], com foco em:

* 🔐 Autenticação baseada em sessão
* 🧩 Arquitetura modular com Blueprints
* 🛡️ Proteção de rotas privadas
* ⚡ Flash Messages dinâmicas
* 🗂️ Organização escalável de código
* 🎯 Separação de responsabilidades
* 🌐 Renderização dinâmica com Jinja2

A aplicação simula um fluxo real de autenticação de usuários em aplicações web modernas, servindo como base para evolução futura em:

* APIs REST
* JWT Authentication
* OAuth
* Banco de dados relacional
* Sistemas multiusuário
* Dashboards administrativos
* Arquiteturas escaláveis

---

# 🧠 Conceitos Aplicados

## ✅ Session Authentication

O projeto utiliza autenticação baseada em sessão:

```python
session['username']
session['token']
```

Após validação das credenciais:

1. O usuário é autenticado
2. A sessão é criada
3. O token é armazenado
4. As rotas privadas são liberadas

---

## ✅ Blueprints

A aplicação utiliza Blueprints do Flask para modularização da arquitetura.

### 📂 Benefícios

* Melhor organização
* Separação de módulos
* Escalabilidade
* Reutilização de código
* Manutenção simplificada
* Arquitetura mais profissional

---

# 🏗️ Estrutura da Aplicação

```bash
project/
│
├── main.py
│
├── routes/
│   ├── auth.py
│   └── user.py
│
├── templates/
│   └── dashboard.html
│
├── .env
│
└── requirements.txt
```

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia                                           | Finalidade            |
| ---------------------------------------------------- | --------------------- |
| Python 3                                             | Linguagem principal   |
| entity["software","Flask","Python web framework"] | Framework web         |
| Jinja2                                               | Template Engine       |
| HTML5                                                | Estrutura frontend    |
| CSS3                                                 | Estilização           |
| dotenv                                               | Variáveis de ambiente |
| Session Authentication                               | Controle de acesso    |
| Flash Messages                                       | Feedback visual       |

---

# 🔄 Fluxo Completo da Aplicação

## 🌍 Fluxo Inicial

```text
Usuário → Página Principal → Login → Dashboard
```

---

# 🔐 Fluxo de Autenticação

## 📥 Login

### Endpoint

```http
/auth/
```

---

## ⚡ Processo de Autenticação

### 1️⃣ Usuário envia credenciais

```python
username = request.form.get('username')
password = request.form.get('pwd')
```

---

### 2️⃣ Sistema valida credenciais

```python
if username == 'admin' and password == 'teste'
```

---

### 3️⃣ Sessão é criada

```python
session['username'] = username
session['token'] = '0000'
```

---

### 4️⃣ Flash Message de sucesso

```python
flash('Login realizado com sucesso.', 'success')
```

---

### 5️⃣ Redirecionamento para Dashboard

```python
return redirect(url_for('user.dashboard'))
```

---

# 🛡️ Middleware de Proteção

O sistema implementa proteção automática de rotas privadas utilizando:

```python
@user_bp.before_request
```

---

## 🔍 Verificação de Sessão

```python
token = session.get('token')
```

---

## 🚫 Caso o usuário não esteja autenticado

```python
return redirect(url_for('auth.login'))
```

---

# 🔓 Fluxo de Logout

## Endpoint

```http
/auth/logout
```

---

## ⚡ Processo de Logout

### Remoção da sessão

```python
session.pop('username', None)
session.pop('token', None)
```

---

### Mensagem de feedback

```python
flash('Logout realizado com sucesso.', 'warning')
```

---

### Redirecionamento

```python
return redirect(url_for('auth.login'))
```

---

# 🧩 Blueprints da Aplicação

# 📂 auth.py

Responsável por:

* 🔐 Login
* 🔓 Logout
* 🎯 Controle de sessão
* ⚡ Flash Messages
* 🔄 Redirecionamentos

---

# 📂 user.py

Responsável por:

* 👤 Dashboard
* ⚙️ Configurações
* 🛡️ Rotas privadas
* 🔒 Middleware de autenticação
* 📦 Controle de acesso

---

# 🖥️ Sistema de Templates

## 📂 dashboard.html

O projeto utiliza templates Jinja2 para:

* renderização dinâmica;
* exibição do usuário autenticado;
* mensagens flash;
* renderização condicional.

---

## 🎨 Flash Messages Dinâmicas

Categorias implementadas:

| Categoria | Estilo      |
| --------- | ----------- |
| success   | 🟢 Verde    |
| warning   | 🟠 Laranja  |
| danger    | 🔴 Vermelho |

---

# 🌐 Rotas do Sistema

# 🌍 Públicas

| Método   | Endpoint | Descrição        |
| -------- | -------- | ---------------- |
| GET      | /        | Página principal |
| GET/POST | /auth/   | Login            |

---

# 🔒 Privadas

| Método | Endpoint        | Descrição         |
| ------ | --------------- | ----------------- |
| GET    | /user/          | Página do usuário |
| GET    | /user/settings  | Configurações     |
| GET    | /user/dashboard | Dashboard         |

---

# 🚨 Tratamento de Erros

O projeto possui:

```python
@app.errorhandler(404)
```

Implementando:

* página personalizada;
* melhor experiência do usuário;
* tratamento de rotas inexistentes.

---

# 🔑 Variáveis de Ambiente

## 📂 Arquivo `.env`

```env
app.secret_key=SEU_SEGREDO
```

---

# ⚙️ Instalação do Projeto

# 📥 Clonar Repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

# 🐍 Criar Ambiente Virtual

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Instalar Dependências

```bash
pip install flask python-dotenv
```

---

# ▶️ Executar Aplicação

```bash
python main.py
```

---

# 🌍 Servidor Local

```http
http://127.0.0.1:5300
```

---

# 🧠 Conceitos Técnicos Demonstrados

✅ Session Authentication
✅ Access Control
✅ Route Protection
✅ Flash Messaging
✅ Jinja2 Templating
✅ Blueprint Architecture
✅ Middleware Validation
✅ Dynamic Rendering
✅ Redirect Flow
✅ Session Persistence
✅ Environment Variables
✅ HTTP Request Handling

---

# 🔐 Segurança Atual

O projeto já demonstra:

* autenticação baseada em sessão;
* controle de acesso;
* proteção de rotas privadas;
* uso de secret key;
* gerenciamento de sessão.

---

# 🚀 Próximas Evoluções

## 🗄️ Banco de Dados

* SQLAlchemy
* PostgreSQL
* MySQL
* SQLite

---

## 🔒 Segurança

* Password Hashing
* JWT Authentication
* CSRF Protection
* Rate Limiting
* Refresh Tokens
* MFA / 2FA

---

## ☁️ Infraestrutura

* Docker
* Docker Compose
* CI/CD
* Nginx
* Cloud Deploy
* VPS

---

## ⚡ Escalabilidade

* Redis
* Celery
* RabbitMQ
* Background Tasks
* Cache
* API REST

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* aprendizado de autenticação web;
* arquitetura Flask profissional;
* modularização de aplicações;
* estruturação de projetos escaláveis;
* boas práticas em aplicações backend.

---

# 👨‍💻 Autor

Projeto desenvolvido utilizando:

* Python
* Flask
* Blueprints
* Session Authentication
* Flash Messages
* Jinja2
* HTML5
* CSS3

---

# ⭐ Considerações Finais

Este projeto representa uma base sólida para evolução em:

* sistemas web completos;
* APIs profissionais;
* autenticação avançada;
* aplicações escaláveis;
* arquitetura backend moderna.

🔥 Estrutura limpa, modular e preparada para expansão futura.
