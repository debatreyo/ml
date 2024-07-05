# DEPENDENCIES

# for working with custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging
# for loading data objects
from src.utils import load_object
# for working with dataframes
import pandas as pd


# PREDICTION PIPELINE
class PredictPipeline:
    """

    """
    # variables
    def __init__(self):
        pass

    # methods
    def predict(self, features):
        try:
            # path for trained model
            model_path = os.path.join("artifact", "model.pkl")
            # path for data preprocessor object
            data_preprocessor_path = os.path.join("artifact", "preprocessor.pkl")
            # load trained model and data preprocessor object
            model = load_object(file_path=model_path)
            data_preprocessor = load_object(file_path=data_preprocessor_path)

            # transform user input data (in form of dataframe) from front-end
            data_scaled = data_preprocessor.transform(features)
            # make prediction
            prediction = model.predict(data_scaled)

            return prediction

        except Exception as e:
            raise CustomException(error_message=e, error_detail=sys)


# CUSTOM DATA
class CustomData:
    """
    Maps the values entered by user
    in front-end of web-app to the
    back-end prediction pipeline.
    """
    # variables
    def __init__(self,
                 gender:str,
                 race_ethnicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 math_score:int,
                 reading_score:int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.math_score = math_score
        self.reading_score = reading_score

    # methods
    def get_data_as_dataframe(self):
        try:
            # dict for creating dataframe
            custom_data_dict = {
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "math_score":[self.math_score],
                "reading_score":[self.reading_score]
            }
            # convert into dataframe and return
            custom_data_df =  pd.DataFrame(data=custom_data_dict)

            logging.info(msg="Successfully mapped input data from web-app front-end into a dataframe")

            return custom_data_df

        except Exception as e:
            raise CustomException(error_message=e, error_detail=sys)
        
        