from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return '<h1>Pagina Principal</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5300)