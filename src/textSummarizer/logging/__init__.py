#we can build a custom log using inbuilt logging module
import os
import sys
import logging
#we define a logging string, whenever we log the info, it will create a file  runninglong.log,
#it will set the timestamp and the it will set the levelname(what kind of logs) then which module are you running(from where are you running the file)
logging_str="{%(asctime)s: %(levelname)s: %(module)s: %(message)s}"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)
#this code will log inside the file and also in the terminal when you run it

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
logger=logging.getLogger("textSummarizerLogger")
