from flask import Flask
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

# rota publica para a pagina principal
@app.route('/')
def root():
    return '<h1>Pagina Principal</h1>'

# Registrar o blueprint do usuário
app.register_blueprint(user_bp, url_prefix='/user')
# Registrar o blueprint de autenticação
app.register_blueprint(auth_bp, url_prefix='/auth')

# rodar servidor
if __name__ == '__main__':
    app.run(debug=True, port=5300)