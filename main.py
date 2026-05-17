from flask import Flask
from routes.user import user_bp

app = Flask(__name__)

@app.route('/')
def root():
    return '<h1>Pagina Principal</h1>'

# Registrar o blueprint do usuário
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True, port=5300)