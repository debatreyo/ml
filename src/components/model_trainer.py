# DEPENDENCIES

# for working with file paths, custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging
# for defining class variables
from dataclasses import dataclass
# for machine learning model building
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
    ) 
from xgboost import XGBRegressor
# for machine learning model evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# utility functions
from src.utils import save_object, evaluate_model



# MODEL TRAINER CONFIG
@dataclass
class ModelTrainerConfig:
    """
    Contains the full file path with filename
    where the final trained machine learning model
    will get saved as a `.pkl` file.
    """
    # file path where final trained model will get saved as a `.pkl` file
    trained_model_file_path:str = os.path.join("artifact", "model.pkl")


# MODEL TRAINER
class ModelTrainer:
    """

    """
    # variables
    def __init__(self):
        # path for storing final trained machine learning model
        self.model_trainer_config = ModelTrainerConfig()

    # methods
    def initiate_model_trainer(self, train_array, test_array):
        """

        """
        try:
            # separate out training and test set into corresponding input & target arrays
            logging.info(msg="Initiating Train-Test split")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1], train_array[:, -1],
                test_array[:, :-1], test_array[:, -1]
            )
            logging.info(msg="Train-Test split completed successfully")

            # declare dict containing all models to try out
            models = {
                "Linear Regression":LinearRegression(),
                "Decision Tree":DecisionTreeRegressor(),
                "KNN Regressor":KNeighborsRegressor(),
                "Ada Boost Regressor":AdaBoostRegressor(),
                "Gradient Boost Regressor":GradientBoostingRegressor(),
                "Random Forest Regressor":RandomForestRegressor(),
                "XGB Regressor":XGBRegressor()
            }
            # declare parameters grid for performing grid search


            # evaluate model
            logging.info(msg="Model training and evaluation initiated")

            model_report:dict = evaluate_model(X_train=X_train, y_train=y_train,
                                               X_test=X_test, y_test=y_test,
                                               models=models)
            logging.info(msg="Model training and evaluation completed successfully")
            
            # extract model with best r2 score on test set
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            # select the best model -> Final model which will be saved and used later
            best_model = models[best_model_name]

            # set threshold for r2 score to accept a model
            if best_model_score < 0.6:
                raise CustomException("No best model found!")

            logging.info(msg="Best model was found and selected successfully")

            # save the best model as `.pkl` file
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            logging.info(msg="Best model was saved as `.pkl` file successfully")

            # use best model to make prediction on test set and evaluate r2 score
            prediction_test = best_model.predict(X_test)
            r2_best_model = r2_score(y_true=y_test, y_pred=prediction_test)

            return best_model_name, r2_best_model

        except Exception as e:
            raise CustomException(error_message=e, error_detail=sys)