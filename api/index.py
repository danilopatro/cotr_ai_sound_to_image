import json
import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/api')
def home():
    return "🤖 A API do Cardboard of the Rings está ONLINE no Vercel!"

@app.route('/timeline', methods=['GET'])
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        # 1. Pega o caminho exato de onde este script está rodando na nuvem
        caminho_pasta = os.path.dirname(__file__)
        caminho_arquivo = os.path.join(caminho_pasta, 'timeline.json')
        
        # 2. Abre o arquivo timeline.json, lê e transforma em código
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_reais = json.load(arquivo)
            
        # 3. Envia os dados reais para o seu Frontend!
        return jsonify(dados_reais)
        
    except FileNotFoundError:
        # Se você esquecer de colocar o arquivo lá, ele avisa
        return jsonify({"erro": "Arquivo timeline.json não encontrado dentro da pasta api."}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500
