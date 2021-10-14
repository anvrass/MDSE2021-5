import os

from flask import jsonify
#from keras.models import load_model
import pickle
import numpy as np
import statsmodels.api as sm


# make prediction
def predict(dataset):
    X = dataset[['Acres', 'Deck', 'GaragCap', 'Patio', 'PkgSpacs', 'Taxes', 'TotBed', 'TotBth', 'TotSqf']]
    y = dataset['SoldPrice']
    X = sm.add_constant(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.pkl")
        #model = load_model(file_path)
        model = pickle.load(open(file_path, 'rb'))
        #val_set2 = dataset.copy()
        model_pred = model.predict(X_test)
        #y_classes = result.argmax(axis=-1)
        #val_set2['class'] = y_classes.tolist()
        #dic = result.to_dict(orient='records')
        #dic = model_pred.to_dict()
        #text_out = {dic}
        return jsonify({'message': 'predicted samples'}), 200
    else:
        return jsonify({'message': 'MODEL_REPO cannot be found.'}), 200
