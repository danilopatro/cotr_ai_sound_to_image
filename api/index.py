import json
import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Esse coringa captura ABSOLUTAMENTE QUALQUER ROTA que cair no Python
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    
    # Se a palavra 'timeline' estiver em qualquer parte do link, entregamos as cartas!
    if 'timeline' in path:
        try:
            caminho_pasta = os.path.dirname(__file__)
            caminho_arquivo = os.path.join(caminho_pasta, 'timeline.json')
            
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                dados_reais = json.load(arquivo)
                
            return jsonify(dados_reais)
            
        except FileNotFoundError:
            return jsonify({"erro": "O arquivo timeline.json não foi encontrado na pasta api"}), 404
            
    # Se não tiver a palavra timeline, mostra uma mensagem de status
    return f"🤖 Flask está rodando perfeitamente! Caminho recebido pela Vercel: /{path}"
