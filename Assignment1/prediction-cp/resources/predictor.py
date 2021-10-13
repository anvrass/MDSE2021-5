import os

from flask import jsonify
#from keras.models import load_model
import pickle
import numpy as np


# make prediction
def predict(dataset):
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.pkl")
        model = pickle.load(open(file_path, 'rb'))
        val_set2 = dataset.copy()
        model_pred = model.predict(dataset)
        val_set2['class'] = y_classes.tolist()
        dic = val_set2.to_dict(orient='records')
        return jsonify(dic), 200
    else:
        return jsonify({'message': 'MODEL_REPO cannot be found.'}), 200