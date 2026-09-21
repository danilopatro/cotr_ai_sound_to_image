import json
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. Quando alguém acessar a página principal (/), o Python entrega o seu index.html
@app.route('/')
def home():
    caminho_pasta = os.path.dirname(__file__)
    return send_from_directory(caminho_pasta, 'index.html')

# 2. Quando o site pedir as cartas, o Python entrega o JSON
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        caminho_pasta = os.path.dirname(__file__)
        caminho_arquivo = os.path.join(caminho_pasta, 'timeline.json')
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_reais = json.load(arquivo)
            
        return jsonify(dados_reais)
        
    except FileNotFoundError:
        return jsonify({"erro": "Arquivo timeline.json não encontrado na pasta api."}), 404
