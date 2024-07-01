# DEPENDENCIES

# for working with custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging
# for working with dataframes
import pandas as pd
# for dataset creation
from sklearn.model_selection import train_test_split
# for defining class variables
from dataclasses import dataclass

# for data transformation
from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation


# DATA INGESTION CONFIG
@dataclass
class DataIngestionConfig:
    """
    Contains essential inputs
    for ingesting data into the
    Machine Learning pipeline.
    """
    # path for storing the raw data
    raw_data_path: str=os.path.join("artifact", "raw.csv") # "\artifact\raw.csv"
    
    # path for storing the training data
    train_data_path: str=os.path.join("artifact", "train.csv") # "\artifact\train.csv"

    # path for storing the test data
    test_data_path: str=os.path.join("artifact", "test.csv") # "\artifact\test.csv"


# DATA INGESTION
class DataIngestion:
    """

    """
    # variables
    def __init__(self):
        # paths for storing ingested data
        self.ingestion_config = DataIngestionConfig()

    # methods

    def initiate_data_ingestion(self):
        logging.info(msg="Entered the data ingestion method/component")
        try:
            # load dataset into Pandas Dataframe
            file_path = r"notebook\data\stud.csv"
            df = pd.read_csv(file_path)
            logging.info(msg="Read the raw dataset into Pandas dataframe")

            # get the directory path where all data is to be stored
            # will use this to create a new directory `artifact`
            data_directory_path = os.path.dirname(self.ingestion_config.raw_data_path)

            # make new directory to store the datasets
            os.makedirs(data_directory_path, exist_ok=True)

            # save the dataframe as csv file into the above created directory with `raw.csv` file name
            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)
            logging.info(msg="Saved the ingested raw data as csv")

            logging.info(msg="Train-Test split initiated")

            # split dataset into training (80% samples) & test set (20% samples)
            train_set, test_set = train_test_split(df, test_size=0.2,
                                                   random_state=42)

            # save training set as csv file
            train_set.to_csv(self.ingestion_config.train_data_path,
                             index=False, header=True)
            # save test set as csv file
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            logging.info(msg="Separate training and test set saved as csv")
            logging.info(msg="Data ingestion completed successfully")


            # return the file paths for training set & test set
            # paths will be needed for loading files during data transformation
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            # raise custom exception with the error message
            raise CustomException(e, sys)



if __name__ == "__main__":
    # create data ingestion object
    data_ingestion_object = DataIngestion()
    # initiate data ingestion process
    train_data_path, test_data_path = data_ingestion_object.initiate_data_ingestion()
    # once this gets executed the `artifact` folder will get created
    # and inside it `raw.csv`, `train.csv`, and `test.csv` will be saved

    # create data transformation object
    data_transformation_object = DataTransformation()
    # initiate data transformation process
    # to get the transformed training set array, test set array,
    # and the data preprocessor object's local file path (not needed right now)
    train_array, test_array, _ = data_transformation_object.initiate_data_transformation(
        train_path=train_data_path,
        test_path=test_data_path
    )