# DEPENDENCIES

# for working with custom exception and custom logging
import os
import sys
from src.exception import CustomException
from src.logger import logging

# for creating web app
from flask import Flask, render_template, request
# for working with dataframes and arrays
import pandas as pd
import numpy as np
# for data processing
from sklearn.preprocessing import StandardScaler
# for transforming the user input (front-end) in to required format
from src.pipeline.predict_pipeline import CustomData
# for making predictions
from src.pipeline.predict_pipeline import PredictPipeline



# WSGI INSTANCE
application = Flask(__name__)

# assign instance to `app` variable for ease of use
app = application


# HOME PAGE
@app.route("/")
def index():
    return render_template("index.html")

# PREDICTION PAGE
@app.route("/predict_data", methods=["GET", "POST"])
def predict_data():
    # if user has not submitted data yet
    if request.method == "GET":
        # show the home page
        return render_template("home.html")

    # if user has submitted the input data via the forms in home page
    elif request.method == "POST":
        gender = request.form.get("gender")
        race_ethnicity = request.form.get("race_ethnicity")
        parental_level_of_education = request.form.get("parental_level_of_education")
        lunch = request.form.get("lunch")
        test_preparation_course = request.form.get("test_preparation_course")
        math_score = request.form.get("math_score")
        reading_score = request.form.get("reading_score")

        # custom data
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            math_score=math_score,
            reading_score=reading_score
        )
        # convert data into dataframe
        data_df = data.get_data_as_dataframe()

        logging.info("Successfully fetched user inputs from front-end in its required format")
        
        # create prediction pipeline object
        prediction_pipeline = PredictPipeline()

        # get model's prediction from the user input
        prediction = (prediction_pipeline.predict(features=data_df))[0] # model prediction is a list with one item (the actual prediction)
        # round off predicted average score
        prediction = round(prediction, ndigits=2)

        logging.info(msg="Model's Prediction for user-input obtained successfully")

        return render_template("home.html", results=prediction)




# RUN WEB APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)