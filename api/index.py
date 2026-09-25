import json
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
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

@app.route('/api/header.jpg', methods=['GET'])
def get_header_image():
    folder_path = os.path.dirname(__file__)
    return send_from_directory(folder_path, 'header.jpg')

@app.route('/api/episodes', methods=['GET'])
def get_available_episodes():
    folder_path = os.path.dirname(__file__)
    local_eps = []
    
    # 1. Lê a pasta local para ver quais JSONs estão disponíveis
    try:
        for filename in os.listdir(folder_path):
            if filename.startswith("timeline_ep") and filename.endswith(".json"):
                ep_num = filename.replace("timeline_ep", "").replace(".json", "")
                local_eps.append(ep_num)
                
        local_eps.sort(key=lambda x: int(x) if x.isdigit() else 0, reverse=True)
    except Exception as e:
        print("Erro ao ler diretório local:", e)

    # 2. Busca e converte o RSS do Libsyn em um dicionário (Config)
    rss_url = "https://cotr.libsyn.com/rss"
    rss_config = {}
    
    try:
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        
        for item in root.findall('./channel/item'):
            title_full = item.find('title').text if item.find('title') is not None else ''
            enclosure = item.find('enclosure')
            audio_url = enclosure.attrib.get('url') if enclosure is not None else ''
            
            # Tenta encontrar o número após "Episode", "CotR" ou isolado
            match = re.search(r'(?:Episode|CotR|Ep)[\s\-]*(\d+)', title_full, re.IGNORECASE)
            if not match:
                match = re.search(r'\b(\d{2,4})\b', title_full)
                
            if match and audio_url:
                ep_num = match.group(1)
                
                # Divide elegantemente o título principal do subtítulo
                if ':' in title_full:
                    parts = title_full.split(':', 1)
                    ep_title = parts[0].strip()
                    ep_subtitle = parts[1].strip()
                elif '-' in title_full:
                    parts = title_full.split('-', 1)
                    ep_title = parts[0].strip()
                    ep_subtitle = parts[1].strip()
                else:
                    ep_title = f"Episode {ep_num}"
                    ep_subtitle = title_full
                    
                rss_config[ep_num] = {
                    "title": ep_title,
                    "subtitle": ep_subtitle,
                    "audioSrc": audio_url
                }
    except Exception as e:
        print("Erro ao processar RSS do Libsyn:", e)

    # Devolve tudo empacotado para o HTML
    return jsonify({
        "available_episodes": local_eps,
        "config": rss_config
    })
