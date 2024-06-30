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
# NOTE: here `06_25_24_09_15_43.log` is the folder getting created
# the actual log file will also have same name as this folder and be stored inside it
logs_path = os.path.join(os.getcwd(),
                         "logs",
                         LOG_FILE)

# create directory using above created path
# exist_ok=True: avoid `FileExistsError` if directory already exists
# if directory does not exist then it will get created
os.makedirs(logs_path, exist_ok=True)

# final full path of the log file
# Example: d:\mlproject\logs\06_25_24_09_15_43.log 
# and inside above folder (06_25_24_09_15_43.log) will be the actual log file of same name (06_25_24_09_15_43) and `.log` extension
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) ## full filepath with filename

# logging format best practice ->
    # Time when log was filed (default format: ‘2003-07-08 16:49:45,896’)
    # line no. in .py script where logging occured
    # log level
    # log message
# Example -> [ 2024-06-30 17:26:20,362 ] 47 root - INFO - Data ingestion completed successfully
# NOTE: `root` is the name the logging module gives to its default logger
format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    filename=LOG_FILE_PATH, # full directory with file name of `.log` file to be created when logging a message
    format=format,          # style format in which log file will be written
    level=logging.INFO      # set root logger to INFO severity level
)

# NOTE: INFO level is used for confirming that program is getting executed as expected