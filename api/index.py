import json
import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    folder_path = os.path.dirname(__file__)
    return send_from_directory(folder_path, 'index.html')

@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    episode_id = request.args.get('ep', '256') 
    
    try:
        folder_path = os.path.dirname(__file__)
        file_name = f'timeline_ep{episode_id}.json'
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            timeline_data = json.load(file)
            
        return jsonify(timeline_data)
        
    except FileNotFoundError:
        return jsonify({"error": f"File {file_name} not found in the api folder."}), 404

# NOVA ROTA: Escaneia a pasta e retorna os episódios disponíveis
@app.route('/api/episodes', methods=['GET'])
def get_available_episodes():
    folder_path = os.path.dirname(__file__)
    episodes = []
    
    try:
        for filename in os.listdir(folder_path):
            if filename.startswith("timeline_ep") and filename.endswith(".json"):
                # Extrai apenas o número (remove 'timeline_ep' e '.json')
                ep_num = filename.replace("timeline_ep", "").replace(".json", "")
                episodes.append(ep_num)
                
        # Ordena de forma decrescente (episódios mais novos primeiro)
        episodes.sort(key=lambda x: int(x) if x.isdigit() else 0, reverse=True)
        return jsonify(episodes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500