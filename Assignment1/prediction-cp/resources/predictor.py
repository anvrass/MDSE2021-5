import os

from flask import jsonify
import pickle
import numpy as np
import statsmodels.api as sm

from sklearn.model_selection import train_test_split


# make prediction
def predict(dataset):
    
    X = dataset[['Acres', 'Deck', 'GaragCap', 'Patio', 'PkgSpacs', 'Taxes', 'TotBed', 'TotBth', 'TotSqf']]
    y = dataset['SoldPrice']
    X = sm.add_constant(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.pkl")
        model = pickle.load(open(file_path, 'rb'))
        
        val_set2 = X_test.copy()
        model_pred = model.predict(X_test)
  
        val_set2['class'] = model_pred
        dic = val_set2.to_dict(orient='records')

        return jsonify(dic), 200
    else:
        return jsonify({'message': 'MODEL_REPO cannot be found.'}), 200
