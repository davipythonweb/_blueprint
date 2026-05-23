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
