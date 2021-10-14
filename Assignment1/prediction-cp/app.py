import pandas as pd
import os
import requests
from flask import Flask, json, request, Response, jsonify

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
    #training = os.environ['TRAINING']
    #r = requests.get(training)
    # receive the prediction request data as the message body
    #content = request.get_json()
    #df = pd.read_json(json.dumps(content), orient='records')
    resp = predictor.predict(df)
    return resp


app.run(host='0.0.0.0', port=5000)
