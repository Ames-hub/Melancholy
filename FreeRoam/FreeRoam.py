import time, sqlite3, logging

# The DB
con = sqlite3.connect('game.db')
cur = con.cursor()

# Logging
logging.basicConfig(filename='logs/FreeRoam.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')