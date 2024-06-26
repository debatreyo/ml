import logging
import os 
from datetime import datetime

# common naming format to be used for log files
# `.strftime()` -> for formatting date objects into readable strings
    # %m: Month as integer (01-12)
    # %d: Day of month (01-31)
    # %Y: Year without century (Ex. 2024 will be 24)
    # %H: Hour (00-23)
    # %M: Minute (00-59) 
    # %S: Second (00-59)
    # Example Log file name: 06_25_24_09_15_43.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# path where log files will get saved
# Example: d:\mlproject\logs\06_25_24_09_15_43.log
logs_path = os.path.join(os.getcwd(),
                         "logs",
                         LOG_FILE)

# create a folder for storing the log files
# exist_ok=True: ensure that if folder/sub-folder already exists then do not raise error,
# instead keep appending files inside it
os.makedirs(logs_path, exist_ok=True)

# final path of the log file
# Example: d:\mlproject\logs\06_25_24_09_15_43.log 
# and inside above folder (06_25_24_09_15_43.log) will be the actual log file of same name (06_25_24_09_15_43) and `.log` extension
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging format best practice ->
    # Time when log was filed
    # line no. in .py script where logging occured
    # log level
    # log message

format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=format,
    level=logging.INFO
)