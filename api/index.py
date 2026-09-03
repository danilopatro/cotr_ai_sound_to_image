from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. Rota de segurança para evitar o erro 404 se você acessar a raiz
@app.route('/')
@app.route('/api')
def home():
    return "🤖 A API do Cardboard of the Rings está ONLINE no Vercel!"

# 2. Rota dupla: garante que funciona mesmo se o Vercel cortar o "/api"
@app.route('/timeline', methods=['GET'])
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    # Cole aqui os dados gerados pelo Google Colab (ou use este teste)
    return jsonify([
        {"tempo_segundos": 5, "nome": "Steward of Gondor", "url": "https://ringsdb.com/bundles/cards/01026.png"},
        {"tempo_segundos": 10, "nome": "A Test of Will", "url": "https://ringsdb.com/bundles/cards/01050.png"},
        {"tempo_segundos": 15, "nome": "Gandalf", "url": "https://ringsdb.com/bundles/cards/01073.png"}
    ])
