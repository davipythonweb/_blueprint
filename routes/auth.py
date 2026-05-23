from flask import Blueprint, request, redirect, url_for, session

# Criar um Blueprint para as rotas relacionadas à autenticação
auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        # Aqui você pode adicionar a lógica de autenticação, como verificar o usuário e senha
        if username == 'admin' and password == 'teste':
            # Simulando a criação de um token de autenticação e armazenando o nome do usuário na sessão
            session['username'] = username
            session['token'] = '0000'  # Simulando um token de autenticação
            return redirect(url_for('user.dashboard'))
        return 'Login falhou. Tente novamente.'

    # Exibir o formulário de login
    return '''
    <div style="text-align: center;border: 1px solid black; padding: 20px; width: 300px; margin: auto;border-radius: 10px;">
    <form method="POST">
        User: <input type="text" name="username"> <br>
        Password: <input type="password" name="pwd"> <br>
        <input type="submit" value="Login">
    </form>
    </div>
    '''

