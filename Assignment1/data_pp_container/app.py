import os

import pandas as pd
import requests
from flask import Flask, json, request, Response

from resources import data_cleaner

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/db_preprocessing/<table_name>', methods=['POST'])
def clean_data(table_name):
    db_api = os.environ['TRAININGDB_API']
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    data_cleaner.clean(df)
    return json.dumps({'message': 'data is cleaned'}, sort_keys=False, indent=4), 200

@app.route('/db_preprocessing/<table_name>', methods=['GET'])
def read_data(table_name):
    db_api = os.environ['TRAININGDB_API']
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    resp = data_cleaner.clean(df)
    return resp

app.run(host='0.0.0.0', port=5006)
