# DEPENDENCIES

# for working with custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging
# for working with dataframes and arrays
import pandas as pd
import numpy as np

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