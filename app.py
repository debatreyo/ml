# DEPENDENCIES

# for creating web app
from flask import Flask, render_template, request
# for working with dataframes and arrays
import pandas as pd
import numpy as np
# for data processing
from sklearn.preprocessing import StandardScaler
# for making predictions



# WEB APP INSTANCE
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
        pass



# RUN WEB APP
