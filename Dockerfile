# fetch a Linux base image for Python interpreter 3.11
FROM python:3.11-slim-buster

# create a new directory named `app`
# and copy entire contents of the project inside it   
COPY . /app

# set current working directory as the `app` folder
# containing all project files & sub-directories
WORKDIR /app

# update all packages and install AWS CLI
RUN apt update -y && apt install awscli -y

# install all dependencies for Flask application to run
RUN pip install -r requirements.txt

# run the Flask web application
CMD ["python", "application.py"]