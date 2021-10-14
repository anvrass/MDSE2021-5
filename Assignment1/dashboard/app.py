import pandas as pd
from flask import Flask, json, request, Response, jsonify

from resources import predictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/dashboard/dash', methods=['POST'])
def predict_perf():
    #training = os.environ['TRAINING']
    #r = requests.get(training)
    # receive the prediction request data as the message body
    resp = dashboard.dash()
    return resp


app.run(host='0.0.0.0', port=5008)
