import os

from flask import jsonify
#from keras.models import load_model
import pickle
import numpy as np


# dumb model summary
def dash():
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.pkl")
        model = pickle.load(open(file_path, 'rb'))
        dic = {'coefficients': model.coef_, 'iterations': model.n_iter_, 'intercept': model.intercept_}
        return jsonify(dic), 200
    else:
        return jsonify({'message': 'MODEL_REPO cannot be found.'}), 200