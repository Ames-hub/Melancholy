# DEFINES GAME-WIDE VARIABLES
name_of_game = "Melancholy"
save_dir = "lib/data/save.json"
standardized_strftime = "%Y.%m.%d_%H-%M-%S"

import os, logging, time
from .printing import printing
# Create the logs directory if it doesn't already exist
logs_dir = 'lib/data/logs'
os.makedirs(logs_dir, exist_ok=True)

from lib.save import *

def save_data(key, value):
    '''Save a specific variable into the save file'''
    jmod.setvalue(
        key=key,
        json_dir=save_dir,
        value=value,
        dt=save_file_dt
    )

def sleep(duration: float=3):
    '''Sleeps for a specified duration. Duration must be a float or int'''
    assert type(float(duration)) is float
    try:
        time.sleep(duration)
    except:
        return "SKIPPED" # Allows for skipping of sleep

def await_choice(question, string="> ", print_faster=("", 0), delay=0, lower=True):
    '''
    Asks a question and returns the user's choice
    Provide a def call to print_type to change the print function
    '''
    printing().delay(text=question, delay=delay, print_faster=print_faster)
    try:
        choice = input("\033[36m"+string+"\033[32m")
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
    return choice.lower() if lower == True else choice

# Creates a Logger
if os.path.exists(logs_dir+"/latest.log"):
    if os.path.exists(logs_dir+"/time_tracker"):
        with open(logs_dir+"/time_tracker", "r") as f:
            last_time = f.read()
    else:
        last_time = time.strftime(standardized_strftime)
        with open(logs_dir+"/time_tracker", "w") as f:
            f.write(last_time)

    new_log_filename = logs_dir+"/" + last_time + ".log"
    
    iteration = 0
    while os.path.exists(new_log_filename):
        iteration += 1
        new_log_filename = f"{logs_dir}/{last_time}_{iteration}.log"

    try:
        os.rename(logs_dir+"/latest.log", new_log_filename)
    except FileExistsError:
        print(f"Failed to rename log file")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='w',
    filename='lib/data/logs/latest.log',
    encoding='utf-8'
)

start_time = time.time()
def get_runtime():
    '''Returns the runtime of the program'''
    return time.time() - start_time

def log(message):
    '''Logs a specified message'''
    logging.info(message)

def logprint(message):
    '''Prints and logs message'''
    print(message)
    logging.info(message)
log("log() and logprint() loaded")