import logging
import os

import pandas as pd
import numpy as np
import pickle

from flask import jsonify


def store(dataset):
    df = dataset
    data_repo = os.environ['DATA_REPO']
    
    if data_repo:
        file_path = os.path.join(data_repo, "predictions.txt")
        df.save(file_path)
        logging.info("Saved the predictions to the location : " + data_repo)
        return jsonify({'message': 'Predictions are saved locally.'}), 200
    else:
        df.save("predictions.txt")
        return jsonify({'message': 'Predictions are saved locally.'}), 200
