from flask import Flask
from flask_cors import CORS
from database import db
from config import Config
from controllers.atividade_route import atividade_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    app.register_blueprint(atividade_bp, url_prefix='/atividade')

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
