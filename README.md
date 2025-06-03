# 📚 Microsserviço de Atividades – Sistema Escolar

Este repositório contém um microsserviço que faz parte do sistema escolar desenvolvido na API principal:  
🔗 https://github.com/Guilherme-alexandr/teste-api-school

Este microsserviço tem como função o gerenciamento de atividades (por professores) e respostas (por alunos), sendo consumido por aplicações clientes ou outros serviços da arquitetura.

⛓️ Este serviço depende da API principal para validar professores e alunos.  
Certifique-se de que a API principal esteja em execução antes de utilizar este microsserviço.

## 📁 Estrutura do Projeto

.
├── app.py  
├── config.py  
├── database.py  
├── models  
│   ├── atividade_model.py  
│   └── resposta_model.py  
├── routes  
│   └── atividade_route.py  
├── requirements.txt  
└── README.md  

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask CORS
- SQLite

## 📌 Funcionalidades

1. Professores podem:
   - Criar atividades
   - Listar todas as atividades
   - Visualizar uma atividade específica
   - Atualizar atividades
   - Excluir atividades

2. Alunos podem:
   - Enviar respostas para uma atividade
   - Listar todas as respostas de uma atividade

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/Guilherme-alexandr/Atividade_Sala
cd Atividade_Sala

2. Instale as dependencias:

pip install -r requirements.txt

3. Inicie a API Principal (Sistema de Gerenciamento):
    Certifique-se de que ela esteja rodando, por padrão no endereço:
    http://192.168.15.18:8000/

4. Rode o microsserviço:
    python app.py

A API ficará disponível por padrão em:
http://localhost:1000/

📨 Exemplo de Requisições JSON
🔸 Criar Atividade (POST /atividade/criar)
{
  "professor_id": 1,
	"turma_id": 1,
  "titulo": "Atividade de Matemática",
  "descricao": "Resolver as equações do PDF",
  "data_entrega": "2025-06-10"
}
🔸 Atualizar Atividade (PUT /atividade/atualizar/1)
{
  "professor_id": 1,
  "titulo": "Atividade de Álgebra",
  "descricao": "Equações do segundo grau",
  "data_entrega": "2025-06-15"
}
🔸 Enviar Resposta (POST /atividade/responder/1)
{
  "atividade_id": 1,
  "aluno_id": 1,
  "resposta": "A resposta está no anexo do PDF",
  "data_envio": "2025-06-05"
}
🔸 Listar Respostas de uma Atividade (GET /atividade/respostas/1)
[
  {
    "id": 1,
    "atividade_id": 1,
    "aluno_id": 1,
    "resposta": "A resposta está no anexo do PDF",
    "data_envio": "2025-06-05"
  }
]
📦 requirements.txt
Flask
Flask-Cors
Flask-SQLAlchemy


