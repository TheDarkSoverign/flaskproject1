from flask import Flask

from config import Config
from app.extensions import db
import pandas as pd


def create_app(config_class=Config):
    app = Flask(__name__)
    app.secret_key = 'qwe'
    app.config.from_object(config_class)

    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.page import bp as page_bp
    app.register_blueprint(page_bp, url_prefix='/page')

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    from app.register import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/register')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/test')
    def test_page():
        return '<h1>Hello World</h1>'

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', port=5000)
