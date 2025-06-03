import requests
from flask import Blueprint, jsonify, request
from models.atividade_model import Atividade
from models.resposta_model import Resposta
from database import db
from config import GERENCIAMENTO_API_URL


atividade_bp = Blueprint('atividade_bp', __name__)


def verificar_professor(id_professor):
    try:
        response = requests.get(f"{GERENCIAMENTO_API_URL}/professor/filtrar/{id_professor}")
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao verificar professor: {e}")
        return False

def verificar_turma(id_turma):
    try:
        response = requests.get(f"{GERENCIAMENTO_API_URL}/turmas/filtrar/{id_turma}")
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao verificar turma: {e}")
        return False
    
def verificar_aluno(id_aluno):
    try:
        response = requests.get(f"{GERENCIAMENTO_API_URL}/aluno/filtrar/{id_aluno}")
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao verificar aluno: {e}")
        return False
    
@atividade_bp.route('/criar', methods=['POST'])
def criar_atividade():
    dados = request.json
    professor_id = dados.get('professor_id')
    turma_id = dados.get('turma_id')
    if not verificar_professor(professor_id):
        return jsonify({"erro": "Professor não encontrado"}), 400

    if not verificar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    nova = Atividade(
        professor_id=professor_id,
        turma_id=turma_id,
        titulo=dados.get('titulo'),
        descricao=dados.get('descricao'),
        data_entrega=dados.get('data_entrega')
    )
    db.session.add(nova)
    db.session.commit()

    return jsonify({"mensagem": "Atividade criada com sucesso!"}), 201

@atividade_bp.route('/listar', methods=['GET'])
def listar_atividades():
    atividades = Atividade.query.all()
    return jsonify([
        {
            "id": atividade.id,
            "professor_id": atividade.professor_id,
            "turma_id": atividade.turma_id,
            "titulo": atividade.titulo
        } for atividade in atividades
    ]), 200

@atividade_bp.route('/filtrar/<int:id>', methods=['GET'])
def filtrar_atividade(id):
    atividade = Atividade.query.get(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada"}), 404

    return jsonify({
        "id": atividade.id,
        "professor_id": atividade.professor_id,
        "turma_id": atividade.turma_id,
        "titulo": atividade.titulo,
        "descricao": atividade.descricao,
        "data_entrega": atividade.data_entrega
    }), 200

@atividade_bp.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar_atividade(id):
    atividade = Atividade.query.get(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada"}), 404
    dados = request.json
    atividade.titulo = dados.get('titulo', atividade.titulo)
    atividade.descricao = dados.get('descricao', atividade.descricao)
    atividade.data_entrega = dados.get('data_entrega', atividade.data_entrega)

    db.session.commit()
    return jsonify({"mensagem": "Atividade atualizada com sucesso!"}), 200

@atividade_bp.route('/deletar/<int:id>', methods=['DELETE'])
def deletar_atividade(id):
    atividade = Atividade.query.get(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada"}), 404

    db.session.delete(atividade)
    db.session.commit()
    return jsonify({"mensagem": "Atividade deletada com sucesso!"}), 200

@atividade_bp.route('/responder/<int:atividade_id>', methods=['POST'])
def responder_atividade(atividade_id):
    dados = request.json
    aluno_id = dados.get('aluno_id')
    resposta_texto = dados.get('resposta')

    atividade = Atividade.query.get(atividade_id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrada"}), 404

    nova_resposta = Resposta(
        atividade_id=atividade_id,
        aluno_id=aluno_id,
        resposta=resposta_texto,
        data_envio=dados.get('data_envio')
    )
    db.session.add(nova_resposta)
    db.session.commit()

    return jsonify({"mensagem": "Resposta enviada com sucesso!"}), 201

@atividade_bp.route('/respostas/<int:atividade_id>', methods=['GET'])
def listar_respostas(atividade_id):
    respostas = Resposta.query.filter_by(atividade_id=atividade_id).all()
    if not respostas:
        return jsonify({"mensagem": "Nenhuma resposta encontrada"}), 404

    return jsonify([
        {
            "id": resposta.id,
            "aluno_id": resposta.aluno_id,
            "resposta": resposta.resposta,
            "data_envio": resposta.data_envio
        } for resposta in respostas
    ]), 200


