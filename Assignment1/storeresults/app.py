import os

import pandas as pd
import requests
from flask import Flask, Response
from flask import jsonify
from resources import model_trainer

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/store/results', methods=['POST'])
def store_results():
    pred_api = os.environ['PRED_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(pred_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    resp = storedata.store(df)
    return resp


app.run(host='0.0.0.0', port=5000)
