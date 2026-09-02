from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite que o seu HTML converse com este servidor

# Aqui você colocaria a lógica do Whisper e do RingsDB que conversamos antes.
# Por enquanto, vamos retornar uma lista gerada pelo Python.
def gerar_timeline_do_podcast():
    return [
    {
        "tempo_segundos": 518,
        "nome": "The One Ring",
        "url": "https://ringsdb.com/bundles/cards/21001.png"
    },
    {
        "tempo_segundos": 1179,
        "nome": "Palantir",
        "url": "https://ringsdb.com/bundles/cards/06090.png"
    },
    {
        "tempo_segundos": 1840,
        "nome": "Wolf",
        "url": "https://ringsdb.com/bundles/cards/302047.png"
    },
    {
        "tempo_segundos": 2420,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 2475,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 2557,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 2608,
        "nome": "Into The West",
        "url": "https://ringsdb.com/bundles/cards/500042.png"
    },
    {
        "tempo_segundos": 2625,
        "nome": "Into The West",
        "url": "https://ringsdb.com/bundles/cards/500042.png"
    },
    {
        "tempo_segundos": 2658,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 2730,
        "nome": "Spare Hood And Cloak",
        "url": "https://ringsdb.com/bundles/cards/131012.png"
    },
    {
        "tempo_segundos": 2740,
        "nome": "Spare Hood And Cloak",
        "url": "https://ringsdb.com/bundles/cards/131012.png"
    },
    {
        "tempo_segundos": 2753,
        "nome": "Into The West",
        "url": "https://ringsdb.com/bundles/cards/500042.png"
    },
    {
        "tempo_segundos": 2811,
        "nome": "Mr. Underhill",
        "url": "https://ringsdb.com/bundles/cards/141017.png"
    },
    {
        "tempo_segundos": 2838,
        "nome": "Bartering",
        "url": "https://ringsdb.com/bundles/cards/18015.png"
    },
    {
        "tempo_segundos": 2983,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 2998,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 3007,
        "nome": "A Test Of Will",
        "url": "https://ringsdb.com/bundles/cards/01050.png"
    },
    {
        "tempo_segundos": 3014,
        "nome": "Hasty Stroke",
        "url": "https://ringsdb.com/bundles/cards/01048.png"
    },
    {
        "tempo_segundos": 3014,
        "nome": "A Test Of Will",
        "url": "https://ringsdb.com/bundles/cards/01050.png"
    },
    {
        "tempo_segundos": 3014,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 3180,
        "nome": "Fellowship",
        "url": "https://ringsdb.com/bundles/cards/21074.png"
    },
    {
        "tempo_segundos": 3193,
        "nome": "Fellowship",
        "url": "https://ringsdb.com/bundles/cards/21074.png"
    },
    {
        "tempo_segundos": 3246,
        "nome": "Gavin",
        "url": "https://ringsdb.com/bundles/cards/301011.png"
    },
    {
        "tempo_segundos": 3343,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 3351,
        "nome": "Drinking Song",
        "url": "https://ringsdb.com/bundles/cards/19116.png"
    },
    {
        "tempo_segundos": 3448,
        "nome": "Gavin",
        "url": "https://ringsdb.com/bundles/cards/301011.png"
    },
    {
        "tempo_segundos": 3489,
        "nome": "Bard Son Of Brand",
        "url": "https://ringsdb.com/bundles/cards/18002.png"
    },
    {
        "tempo_segundos": 3525,
        "nome": "Into The West",
        "url": "https://ringsdb.com/bundles/cards/500042.png"
    },
    {
        "tempo_segundos": 3603,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 3637,
        "nome": "Dale Messenger",
        "url": "https://ringsdb.com/bundles/cards/22111.png"
    },
    {
        "tempo_segundos": 4034,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 4136,
        "nome": "North Realm Lookout",
        "url": "https://ringsdb.com/bundles/cards/18004.png"
    },
    {
        "tempo_segundos": 4256,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 4308,
        "nome": "Determination",
        "url": "https://ringsdb.com/bundles/cards/10172.png"
    },
    {
        "tempo_segundos": 4308,
        "nome": "Valiant Determination",
        "url": "https://ringsdb.com/bundles/cards/19092.png"
    },
    {
        "tempo_segundos": 4349,
        "nome": "Wild Stallion",
        "url": "https://ringsdb.com/bundles/cards/19033.png"
    },
    {
        "tempo_segundos": 4365,
        "nome": "Wild Stallion",
        "url": "https://ringsdb.com/bundles/cards/19033.png"
    },
    {
        "tempo_segundos": 4419,
        "nome": "Determination",
        "url": "https://ringsdb.com/bundles/cards/10172.png"
    },
    {
        "tempo_segundos": 4419,
        "nome": "Valiant Determination",
        "url": "https://ringsdb.com/bundles/cards/19092.png"
    },
    {
        "tempo_segundos": 4487,
        "nome": "Fellowship",
        "url": "https://ringsdb.com/bundles/cards/21074.png"
    },
    {
        "tempo_segundos": 4496,
        "nome": "Determination",
        "url": "https://ringsdb.com/bundles/cards/10172.png"
    },
    {
        "tempo_segundos": 4532,
        "nome": "Bartering",
        "url": "https://ringsdb.com/bundles/cards/18015.png"
    },
    {
        "tempo_segundos": 4707,
        "nome": "Bartering",
        "url": "https://ringsdb.com/bundles/cards/18015.png"
    },
    {
        "tempo_segundos": 4713,
        "nome": "Bartering",
        "url": "https://ringsdb.com/bundles/cards/18015.png"
    },
    {
        "tempo_segundos": 4821,
        "nome": "Hasty Stroke",
        "url": "https://ringsdb.com/bundles/cards/01048.png"
    },
    {
        "tempo_segundos": 4825,
        "nome": "Hasty Stroke",
        "url": "https://ringsdb.com/bundles/cards/01048.png"
    },
    {
        "tempo_segundos": 4835,
        "nome": "Hasty Stroke",
        "url": "https://ringsdb.com/bundles/cards/01048.png"
    },
    {
        "tempo_segundos": 4880,
        "nome": "North Realm Lookout",
        "url": "https://ringsdb.com/bundles/cards/18004.png"
    },
    {
        "tempo_segundos": 5041,
        "nome": "Open The Armory",
        "url": "https://ringsdb.com/bundles/cards/17118.png"
    },
    {
        "tempo_segundos": 5049,
        "nome": "Valor",
        "url": "https://ringsdb.com/bundles/cards/01133.png"
    },
    {
        "tempo_segundos": 5063,
        "nome": "Valor",
        "url": "https://ringsdb.com/bundles/cards/01133.png"
    },
    {
        "tempo_segundos": 5092,
        "nome": "Valor",
        "url": "https://ringsdb.com/bundles/cards/01133.png"
    },
    {
        "tempo_segundos": 5131,
        "nome": "Traffic From Dale",
        "url": "https://ringsdb.com/bundles/cards/18012.png"
    },
    {
        "tempo_segundos": 5161,
        "nome": "Traffic From Dale",
        "url": "https://ringsdb.com/bundles/cards/18012.png"
    },
    {
        "tempo_segundos": 5263,
        "nome": "Resourceful",
        "url": "https://ringsdb.com/bundles/cards/04062.png"
    },
    {
        "tempo_segundos": 5272,
        "nome": "Traffic From Dale",
        "url": "https://ringsdb.com/bundles/cards/18012.png"
    },
    {
        "tempo_segundos": 5462,
        "nome": "Drinking Song",
        "url": "https://ringsdb.com/bundles/cards/19116.png"
    },
    {
        "tempo_segundos": 5473,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 5478,
        "nome": "Drinking Song",
        "url": "https://ringsdb.com/bundles/cards/19116.png"
    },
    {
        "tempo_segundos": 5489,
        "nome": "Drinking Song",
        "url": "https://ringsdb.com/bundles/cards/19116.png"
    },
    {
        "tempo_segundos": 5569,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 5581,
        "nome": "Song Of Healing",
        "url": "https://ringsdb.com/bundles/cards/22112.png"
    },
    {
        "tempo_segundos": 5599,
        "nome": "King Of Dale",
        "url": "https://ringsdb.com/bundles/cards/18008.png"
    },
    {
        "tempo_segundos": 5613,
        "nome": "Song Of Hope",
        "url": "https://ringsdb.com/bundles/cards/17082.png"
    },
    {
        "tempo_segundos": 5613,
        "nome": "Song Of Healing",
        "url": "https://ringsdb.com/bundles/cards/22112.png"
    },
    {
        "tempo_segundos": 5673,
        "nome": "Ancestral Armor",
        "url": "https://ringsdb.com/bundles/cards/19028.png"
    },
    {
        "tempo_segundos": 5736,
        "nome": "Drinking Song",
        "url": "https://ringsdb.com/bundles/cards/19116.png"
    },
    {
        "tempo_segundos": 6343,
        "nome": "Second Breakfast",
        "url": "https://ringsdb.com/bundles/cards/02027.png"
    }
]

# Cria a rota da API
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    dados_cartas = gerar_timeline_do_podcast()
    return jsonify(dados_cartas) # Converte a lista do Python para JSON
