import requests
from flask import Blueprint, jsonify, request
from models.atividade_model import Atividade, Resposta
from database import db
from config import GERENCIAMENTO_API_URL


atividade_bp = Blueprint('atividade_bp', __name__, url_prefix='/atividades')


def professor_existe(id_professor):
    url = f"{GERENCIAMENTO_API_URL}{id_professor}"
    try:
        response = requests.get(url)
        return response.status_code == 200 and response.json() != {}
    except requests.exceptions.RequestException:
        return False


# 🔸 Listar atividades
@atividade_bp.route('/', methods=['GET'])
def listar_atividades():
    atividades = Atividade.query.all()
    resultado = []
    for atividade in atividades:
        resultado.append({
            'id': atividade.id,
            'id_disciplina': atividade.id_disciplina,
            'id_professor': atividade.id_professor,
            'enunciado': atividade.enunciado
        })
    return jsonify(resultado)


# 🔸 Obter uma atividade específica
@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if atividade is None:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

    respostas = [ 
        {
            'id': r.id,
            'id_aluno': r.id_aluno,
            'resposta': r.resposta,
            'nota': r.nota
        } for r in atividade.respostas
    ]

    return jsonify({
        'id': atividade.id,
        'id_disciplina': atividade.id_disciplina,
        'id_professor': atividade.id_professor,
        'enunciado': atividade.enunciado,
        'respostas': respostas
    })


# 🔸 Criar uma nova atividade (com validação do professor)
@atividade_bp.route('/', methods=['POST'])
def criar_atividade():
    dados = request.get_json()

    if not professor_existe(dados['id_professor']):
        return jsonify({'erro': 'Professor não encontrado na API principal'}), 404

    nova_atividade = Atividade(
        id_disciplina=dados['id_disciplina'],
        id_professor=dados['id_professor'],
        enunciado=dados['enunciado']
    )
    db.session.add(nova_atividade)
    db.session.commit()

    return jsonify({'mensagem': 'Atividade criada com sucesso', 'id': nova_atividade.id}), 201


# 🔸 Adicionar uma resposta (sem validação de aluno)
@atividade_bp.route('/<int:id_atividade>/respostas', methods=['POST'])
def adicionar_resposta(id_atividade):
    dados = request.get_json()

    atividade = Atividade.query.get(id_atividade)
    if atividade is None:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

    nova_resposta = Resposta(
        id_atividade=id_atividade,
        id_aluno=dados['id_aluno'],
        resposta=dados['resposta'],
        nota=dados.get('nota')
    )
    db.session.add(nova_resposta)
    db.session.commit()

    return jsonify({'mensagem': 'Resposta registrada com sucesso', 'id': nova_resposta.id}), 201


# Rota para verificar se a API está funcionando corretamente
@atividade_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200