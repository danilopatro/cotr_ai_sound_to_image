import json
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. When someone accesses the main page (/), Python serves the index.html
@app.route('/')
def home():
    folder_path = os.path.dirname(__file__)
    return send_from_directory(folder_path, 'index.html')

# 2. When the site requests the cards, Python delivers the JSON
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    try:
        folder_path = os.path.dirname(__file__)
        file_path = os.path.join(folder_path, 'timeline.json')
        
        with open(file_path, 'r', encoding='utf-8') as file:
            timeline_data = json.load(file)
            
        return jsonify(timeline_data)
        
    except FileNotFoundError:
        return jsonify({"error": "File timeline.json not found in the api folder."}), 404
