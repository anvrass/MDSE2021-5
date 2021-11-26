import concurrent.futures
import os

import flask
import pandas as pd
import requests
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def main():
    client = bigquery.Client(project="de2021-325520")  # use your project id

    QUERY = (
        'SELECT * FROM `de2021-325520.a2_dataset.products` LIMIT 100')  # use the correct project id, etc.
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    return flask.redirect(
        flask.url_for(
            "results",
            project_id=query_job.project,
            job_id=query_job.job_id,
            location=query_job.location
        )

    )


@app.route('/results', methods=['POST'])
def results():
    client = bigquery.Client(project="de2021-325520")  # use your project id

    QUERY = (
        'SELECT * FROM `de2021-325520.a2_dataset.products` LIMIT 100')  # use the correct project id, etc.
    query_job = client.get_job(project="de2021-325520")
    try:
        results = query_job.result(timeout=30)
    except concurrent.futures.TimeoutError:
        return flask.render_template("timeout.html", job_id = query_job.job_id)

    return flask.render_template("query_result.html", results = results)

app.run(port=5000)
