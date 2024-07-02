# DEPENDENCIES

# for working with custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging
# for working with dataframes and arrays
import pandas as pd
import numpy as np
# for machine learning model evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# for saving objects
import dill


# utility function 1
def save_object(file_path:str, obj):
    """
    Generic utility function for
    saving various data objects
    in the input file path.

    Input Parameters ->
    `file_path`: (str) The relative path where object is to be saved
    `obj`: The object which is to be saved
    """
    try:
        # get directory path where object is to be saved
        dir_path = os.path.dirname(file_path)
        # create directory if it does not exist already
        os.makedirs(dir_path, exist_ok=True)

        # save the object
        with open(file_path, "wb") as file_object:
            dill.dump(obj, file_object)

        logging.info(msg="Object saved successfully")
        
    except Exception as e:
        raise CustomException(error_message=e, error_detail=sys)


# utility function 2
def evaluate_model(X_train, y_train,
                   X_test, y_test,
                   models:dict):
    """
    Trains the input machine learning models,
    evaluates its performance on Test set
    using R^2 (Coefficient of Determination) metric.

    Returns a `report` (dict) containing
    model's name as key and R^2 score as value.
    
    Input Parameters ->
    X_train, y_train: (array) Training set
    X_test, y_test: (array) Test set
    models: (dict) contains machine learning models to be evaluated.
            key: model name (str)
            value: model instance (untrained) 
    """
    try:
        # for storing the evaluation scores for each model
        report = {}

        models_names:str = list(models.keys())      # Names of models
        models_objects = list(models.values())      # Instances of models

        # iterate over all models and train-predict-evaluate
        for i in range(len(models_names)):
            # get the model object
            model = models_objects[i]

            # fit model to training set
            model.fit(X_train, y_train)
            
            # predict on training and test sets
            y_train_predictions = model.predict(X_train)
            y_test_predictions = model.predict(X_test)

            # evaluate model performance
            train_model_score = r2_score(y_true=y_train, y_pred=y_train_predictions)
            test_model_score = r2_score(y_true=y_test, y_pred=y_test_predictions)

            # store test set evaluation result for current model
            report[models_names[i]] = test_model_score

        return report
          

    except Exception as e:
        raise CustomException(error_message=e, error_detail=sys)