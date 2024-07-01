# DEPENDENCIES

# for working with file paths, custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging
# for working with dataframes
import pandas as pd
# for defining class variables
from dataclasses import dataclass
# for data transformations
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# for saving data objects
from src.utils import save_object


# DATA TRANSFORMATION CONFIG
@dataclass
class DataTransformationConfig:
    """
    Contains essential inputs
    for data transformation
    in the Machine Learning pipeline.
    """
    # path for storing the final data processor pipeline object (`.pkl` file)
    preprocessor_object_file_path = os.path.join("artifact", "preprocessor.pkl") ## \artifact\preprocessor.pkl


# DATA TRANSFORMATION
class DataTransformation:
    """

    """
    # variables
    def __init__(self):
        # path for storing final preprocessor pipeline object
        self.data_transformation_config = DataTransformationConfig()

    # methods
    def get_data_transformer_object(self):
        """
        Returns a data transformation object
        which can be used to perform various transformations
        on the numerical and categorical columns/features
        of the dataset.
        """
        try:
            # specify columns as per datatype for applying transformation
            numerical_features = [
                "math_score", "reading_score"
            ]
            categorical_features = [
                "gender", "race_ethnicity",
                "parental_level_of_education",
                "test_preparation_course", "lunch"
            ]
            # separate pipeline objects for separate datatypes
            numerical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])
            categorical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))             # `with_mean=False` to disable centering the Sparse matrix and make computation efficient
            ])

            logging.info(msg="Numerical columns transformations completed successfully")

            logging.info(msg="Categorical columns transformations completed successfully")

            # create Column transformation pipeline
            preprocessor = ColumnTransformer(transformers=[
                ("numerical_transformer", numerical_pipeline, numerical_features),
                ("categorical_transformer", categorical_pipeline, categorical_features)
            ])

            # return the final preprocessor object
            return preprocessor
        
        except Exception as e:
            raise CustomException(error_message=e, error_detail=sys)


    def initiate_data_transformation(self, train_path, test_path):
        """

        """
        try:
            # get training and test dataset as a dataframe
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info(msg="Training and Test set read as dataframes successfully")

            logging.info(msg="Initiating fetching data preprocessor object")

            # get data preprocessor
            data_preprocessor = self.get_data_transformer_object()

            logging.info(msg="Data preprocessor object fetched successfully")

            # create `avg_score` target variable in both dataframes
            # drop `writing_score` column in both dataframes
            train_df["avg_score"] = (train_df["math_score"] + train_df["writing_score"] + train_df["reading_score"])/3
            train_df.drop(columns=["writing_score"], inplace=True)
            
            test_df["avg_score"] = (test_df["math_score"] + test_df["writing_score"] + test_df["reading_score"])/3
            test_df.drop(columns=["writing_score"], inplace=True)

            logging.info(msg="Feature engineering performed by creating `avg_score` target variable feature")

            # target column name
            target_col_name = "avg_score"

            # separate input features and target variable
            input_features_train_df = train_df.drop(columns=[target_col_name])
            target_feature_train_df = train_df[target_col_name]

            input_features_test_df = test_df.drop(columns=[target_col_name])
            target_feature_test_df = test_df[target_col_name]

            logging.info(msg="Input features and target variable separated for both training and test set")

            logging.info(msg="Initiating applying data preprocessor object to training and test input datasets")

            # pass training and test set input features through data preprocessor pipeline to obtain sparse arrays
            input_features_train_array = data_preprocessor.fit_transform(input_features_train_df)

            input_features_test_array = data_preprocessor.transform(input_features_test_df)

            logging.info(msg="Application of data preprocessor object to training and test input datasets completed successfully")

            # create final preprocessed training and test set arrays
            train_array = np.c_[
                input_features_train_array,
                np.array(target_feature_train_df)
            ]

            test_array = np.c_[
                input_features_test_array,
                np.array(target_feature_test_df)
            ]

            logging.info(msg="Transformed Training and Test array created successfully")

            # save the data preprocessor object as `.pkl` file in the defined file path
            save_object(
                file_path=self.data_transformation_config.preprocessor_object_file_path,
                obj=data_preprocessor
            )

            logging.info(msg="Saved Data preprocessor as a `.pkl` file successfully")

            return (
                train_array, test_array,
                self.data_transformation_config.preprocessor_object_file_path
            )

            
             

            

            

            
            

            

        except Exception as e:
            raise CustomException(error_message=e, error_detail=sys)