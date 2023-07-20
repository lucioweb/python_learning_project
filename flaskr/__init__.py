import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

 # Importe e registre o blueprint da fábrica usando app.register_blueprint().
 # Coloque o novo código no final da função de fábrica antes de devolver o aplicativo.
 # O blueprint de autenticação terá visualizações para cadastrar novos usuários e efetuar login e logout.
    from . import auth
    app.register_blueprint(auth.bp)

    # BLOG
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
