from flask import Blueprint, flash, request, redirect, url_for, session, render_template_string

# Criar um Blueprint para as rotas relacionadas à autenticação
auth_bp = Blueprint('auth', __name__, template_folder='templates')

# rota de login para autenticar o usuário
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')

        if username == 'admin' and password == 'teste':
            session['username'] = username
            session['token'] = '0000'

            flash('Login realizado com sucesso.', 'success')
            return redirect(url_for('user.dashboard'))

        flash('Login falhou. Tente novamente.', 'danger')

    return render_template_string('''
    <div style="
        text-align: center;
        border: 1px solid black;
        padding: 20px;
        width: 300px;
        margin: auto;
        border-radius: 10px;
    ">

    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, message in messages %}
          <div style="
              padding:10px;
              margin-bottom:10px;
              border-radius:5px;
              background-color:
              {% if category == 'success' %}
                  lightgreen
              {% elif category == 'warning' %}
                  orange
              {% elif category == 'danger' %}
                  #ff9999
              {% endif %}
          ">
            {{ message }}
          </div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <form method="POST">
        User:<br>
        <input type="text" name="username"><br><br>

        Password:<br>
        <input type="password" name="pwd"><br><br>

        <input type="submit" value="Login">
    </form>

    </div>
    ''')


# fazer logout com flask message e redirect para a pagina de login
@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('token', None)

    flash('Logout realizado com sucesso.', 'warning')
    return redirect(url_for('auth.login'))


# esta menssagem nao apareceu na tela? porque? porque nao tem um template para exibir as mensagens flash, entao a mensagem é armazenada na sessão, mas não é exibida em nenhum lugar. Para exibir as mensagens flash, você precisa adicionar um código no seu template para renderizar as mensagens. Por exemplo, no seu template HTML, você pode adicionar o seguinte código para exibir as mensagens flash:
"""
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul>
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
"""

