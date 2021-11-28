import concurrent.futures
import os

import flask
import pandas as pd
import requests
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/results', methods=['GET'])
def results():
    client = bigquery.Client(project="de2021-325520")  # use your project id

    QUERY = (
        'SELECT * FROM `de2021-324520.a2dataset.products` LIMIT 100')  # use the correct project id, etc.
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()

    for row in rows:
        output = "Record: " + str(row)
    return output


app.run(host='0.0.0.0',port=5000)
