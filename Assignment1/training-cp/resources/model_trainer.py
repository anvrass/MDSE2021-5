# MLP for Pima Indians Dataset saved to single file
# see https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import logging
import os

from flask import jsonify
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

def train(dataset):
    # We drop Latitude and Longitude from the set as they do little to serve as predictors for price.
    # To prevent overfitting the model, no further variables will be dropped.

    X = dataset[['Acres', 'Deck', 'GaragCap', 'Patio', 'PkgSpacs', 'Taxes', 'TotBed', 'TotBth', 'TotSqf']]
    y = dataset['SoldPrice']
    X = sm.add_constant(X)

    # We now wiull use scikitlearn's train_test_split to split our set into a training and a testing set for our
    # X and y. I will do this in a way to prepare for a 5-fold cross validation. 
    # once this is done, we use te train data to train our model and use the test data to see how well our prediction fits
    # the test data.
    # We generate a prediction

    # We shall use R_squared as a metric of how well the model fits the test data.

    r2_vals = []

    for i in range(10) :

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
        model = sm.OLS(y_train, X_train).fit()
        model_pred = model.predict(X_test)
        r2_vals.append(r2(y_test, model_pred))

    print('Mean R-Squared over 10 runs: ' + str(np.mean(r2_vals))) 
    print("")
    text_out = {model.summary()}

    # Of all variables used in the model, two stand out to be particularly good for price prediction being Taxes and TotSqf
    # with both their standard error being ~7 and ~11 respectively. they are followed by PkgSpacs, having a standard 
    # error of ~3728. All other variables have a standard error that ios at least almost twice the standard error of 
    # PkgSpacs.

    # Using 5-fold cross validation, we tend to average around 0.8 for our R-Squared value.
    # While close and fairly impressive by itself, it is not accurate enough to beat the R-Squared score
    # of List Price vs SoldPrice at 0.991

    ridge_reg = Ridge(alpha=10, fit_intercept=True)
    ridge_reg.fit(X_train, y_train)

    cols = ['const','Acres', 'Deck', 'GaragCap', 'Patio', 'PkgSpacs', 'Taxes', 'TotBed', 'TotBth', 'TotSqf']
    print("Ridge regression model:\n {}+ {}^T . X".format(ridge_reg.intercept_, ridge_reg.coef_))
    pd.Series(ridge_reg.coef_.flatten(), index=cols)

    # We can see that as a result of the regularization, the coeffiecients have normalized to lower values.

    # Saving model in a given location provided as an env. variable
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "model.h5")
        model.save(file_path)
        logging.info("Saved the model to the location : " + model_repo)
        return jsonify(text_out), 200
    else:
        model.save("model.h5")
        return jsonify({'message': 'The model was saved locally.'}), 200
