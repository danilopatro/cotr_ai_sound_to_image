from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite que o seu HTML converse com este servidor

# Aqui você colocaria a lógica do Whisper e do RingsDB que conversamos antes.
# Por enquanto, vamos retornar uma lista gerada pelo Python.
def gerar_timeline_do_podcast():
    return [
        {"tempo_segundos": 5, "nome": "Steward of Gondor", "url": "https://ringsdb.com/bundles/cards/01026.png"},
        {"tempo_segundos": 10, "nome": "A Test of Will", "url": "https://ringsdb.com/bundles/cards/01050.png"},
        {"tempo_segundos": 15, "nome": "Gandalf", "url": "https://ringsdb.com/bundles/cards/01073.png"}
    ]

# Cria a rota da API
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    dados_cartas = gerar_timeline_do_podcast()
    return jsonify(dados_cartas) # Converte a lista do Python para JSON
