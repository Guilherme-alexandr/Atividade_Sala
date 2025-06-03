import os

class Config:
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 1000))
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///atividade.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

GERENCIAMENTO_API_URL = "http://192.168.15.18:8000"