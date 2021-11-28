import concurrent.futures
import os

import flask
import pandas as pd
import requests
from flask import Flask, json, request, Response
from google.cloud import bigquery

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/results', methods=['GET'])
def results():
    client = bigquery.Client(project="de2021-325520")  # use your project id
    
    table_ref = client.dataset("a2_dataset").table("products")
    
    table = client.get_table(table_ref)
    
    df = client.list_rows(table).to_dataframe
    resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    return resp
    #QUERY = (
    #    'SELECT * FROM `de2021-325520.a2_dataset.products` LIMIT 100')  # use the correct project id, etc.
    #query_job = client.query(QUERY)  # API request
    #rows = query_job.result()

    #for row in rows:
        output = "Record: " + str(row)
    #return output


app.run(host='0.0.0.0',port=5000)
