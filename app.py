from flask import Flask
from database import db
from config import Config
from routes.atividade_route import atividade_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(atividade_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
