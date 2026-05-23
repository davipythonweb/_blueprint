from flask import Flask, render_template_string
from dotenv import load_dotenv
import os

# importar blueprints
from routes.user import user_bp
from routes.auth import auth_bp

# Carregar variáveis de ambiente
load_dotenv()
# Criar a aplicação Flask
app = Flask(__name__)
# Definir a chave secreta para a sessão (pode ser definida em um arquivo .env)
app.secret_key = os.getenv('app.secret_key')

# tratar erros 404 com uma página personalizada
@app.errorhandler(404)
def page_not_found(e):
    return render_template_string('''
    <div style="
        padding:20px;
        margin:20px;
        background-color:#f2f2f2;
    ">
        <h1>ERRO 404! PAGE NOT FOUND!</h1>
        <h2>Ops! A página que você está procurando não existe.</h2>
        <p>Verifique se o URL está correto ou volte para a <a href="/">página principal</a>.</p>
    </div>
    ''')


# rota publica para a pagina principal
@app.route('/')
def root():
    return render_template_string('''
        <h1>Pagina Principal</h1>
        ''')

# Registrar o blueprint do usuário
app.register_blueprint(user_bp, url_prefix='/user')
# Registrar o blueprint de autenticação
app.register_blueprint(auth_bp, url_prefix='/auth')

# rodar servidor
if __name__ == '__main__':
    app.run(debug=True, port=5300)