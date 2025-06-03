from database import db

class Resposta(db.Model):
    table_name = 'respostas'

    id = db.Column(db.Integer, primary_key=True)
    atividade_id = db.Column(db.Integer, nullable=False)
    aluno_id = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.String(20), nullable=False)