from database import db


class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, nullable=False)
    id_professor = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(255), nullable=False)

    respostas = db.relationship('Resposta', backref='atividade', cascade='all, delete-orphan')


class Resposta(db.Model):
    __tablename__ = 'respostas'

    id = db.Column(db.Integer, primary_key=True)
    id_atividade = db.Column(db.Integer, db.ForeignKey('atividades.id'), nullable=False)
    id_aluno = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.String(255), nullable=False)
    nota = db.Column(db.Float, nullable=True)
