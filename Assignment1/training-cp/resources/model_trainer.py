# MLP for Pima Indians Dataset saved to single file
# see https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import logging
import os

import pandas as pd
import numpy as np
import pickle

from flask import jsonify
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score as r2

def train(dataset):
    # We drop Latitude and Longitude from the set as they do little to serve as predictors for price.
    # To prevent overfitting the model, no further variables will be dropped.

    X = dataset[['Acres', 'Deck', 'GaragCap', 'Patio', 'PkgSpacs', 'Taxes', 'TotBed', 'TotBth', 'TotSqf']]
    y = dataset['SoldPrice']
    X = sm.add_constant(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
    ridge_reg = Ridge(alpha=10, fit_intercept=True)
    ridge_reg.fit(X_train, y_train)

    cols = ['const','Acres', 'Deck', 'GaragCap', 'Patio', 'PkgSpacs', 'Taxes', 'TotBed', 'TotBth', 'TotSqf']
    #print("Ridge regression model:\n {}+ {}^T . X".format(ridge_reg.intercept_, ridge_reg.coef_))
    text_out = {print("Ridge regression model:\n {}+ {}^T . X".format(ridge_reg.intercept_, ridge_reg.coef_))}
    pd.Series(ridge_reg.coef_.flatten(), index=cols)

    # Saving model in a given location provided as an env. variable
    model_repo = os.environ['MODEL_REPO']
    model = ridge_reg
    
    if model_repo:
        file_path = os.path.join(model_repo, "model.pkl")
        #model.save(file_path)
        pickle.dump(model, open(file_path,'wb'))
        logging.info("Saved the model to the location : " + model_repo)
        return jsonify(text_out), 200
    else:
        #model.save("model.h5")
        pickle.dump(model,"model.pkl")
        return jsonify({'message': 'The model was saved locally.'}), 200
