from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def root():
    return '''
    <h1>Pagina do Usuario</h1>
    '''

@user_bp.route('/settings')
def settings():
    return '''
    <h1>Pagina de Configurações do Usuario</h1>
    '''

@user_bp.route('/dashboard')
def dashboard():
    name = "Davi - "
    return render_template('dashboard.html', name = name)







"""
Com o Blueprint, podemos organizar melhor as rotas relacionadas ao usuário em um módulo separado.
 Isso torna o código mais modular e fácil de manter, especialmente à medida que a aplicação cresce.
   O Blueprint permite que você defina rotas, templates e outros recursos relacionados ao 
   usuário em um único lugar, facilitando a reutilização e a organização do código. 
   No exemplo acima, criamos um Blueprint chamado 'user_bp' e definimos duas rotas:
1. A rota '/' que retorna uma página principal para o usuário.
2. A rota '/settings' que retorna uma página de configurações para o usuário.
Essas rotas são registradas no aplicativo principal usando o método 'register_blueprint',
    com um prefixo de URL '/user'. Isso significa que as rotas definidas no Blueprint estarão
    acessíveis através de URLs como '/user/' e '/user/settings'.    

"""