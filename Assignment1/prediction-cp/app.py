import pandas as pd
from flask import Flask, json, request, Response, jsonify
import os
import requests
from resources import predictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/prediction-cp/results', methods=['POST'])
def predict_perf():  
    db_api = os.environ['DB_API']
    # Make a GET request to training db service to retrieve the prediction data/features.
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    resp = predictor.predict(df)
    return resp


app.run(host='0.0.0.0', port=5000)
