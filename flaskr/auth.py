import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# REGISTRO


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Nome de usuário é obrigatório.'
        elif not password:
            error = 'Senha é campo de preenchimento obrigatório.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} já está registrado em nossa base de dados."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

# LOGIN


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Nome de usuário incorreto!.'
        elif not check_password_hash(user['password'], password):
            error = 'Senha incorreta.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# Agora que o do usuário idestá armazenado no session, ele estará disponível nas solicitações subsequentes.
# No início de cada solicitação, se um usuário estiver logado, suas informações devem ser carregadas e
# disponibilizadas para outras visualizações.


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# Sair
# Para sair, você precisa remover o ID do usuário do arquivo session.
# Em seguida, "load_logged_in_user" não carregará um usuário nas solicitações subsequentes.


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Criar, editar e excluir postagens de blog exigirá que um usuário esteja conectado.
# Um decorador pode ser usado para verificar isso para cada visualização à qual é aplicado.


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
