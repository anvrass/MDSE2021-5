import os
import requests
from flask import Flask, Response
from flask import jsonify
from resources import model_trainer

app = Flask(__name__, static_folder = "static")
app.config["DEBUG"] = True


@app.route('/dashboard/dash', methods=['POST'])
def dashboard():
    dashboard.show_images(im)
    return render_template('dash.html')

app.run(host='0.0.0.0', port=5008)
