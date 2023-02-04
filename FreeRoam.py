
# Remember to fix the bullshit that is the weather system. Seriously, it's a mess.
# Returns "DISABLED" or "Weather" when it shouldn't. I don't know why.

import time, sqlite3, logging, random, os, sys, colorama

# Imports trauma and health and stamina from the DB

# The DB
con = sqlite3.connect('melancholy.db')
cur = con.cursor()

logging.info("Importing stats from DB")
cur.execute("SELECT trauma FROM stats")
trauma = cur.fetchone()[0]

cur.execute("SELECT debug FROM dev")
debug = cur.fetchone()[0]

# Imports all stats from db one by one
cur.execute("SELECT health FROM stats")
health = cur.fetchone()[0]
cur.execute("SELECT maxhealth FROM stats")
maxhealth = cur.fetchone()[0]
cur.execute("SELECT stamina FROM stats")
stamina = cur.fetchone()[0]
cur.execute("SELECT maxstamina FROM stats")
maxstamina = cur.fetchone()[0]
cur.execute("SELECT minstamina FROM stats")
minstamina = cur.fetchone()[0]
cur.execute("SELECT money FROM stats")
money = cur.fetchone()[0]
cur.execute("SELECT minmoney FROM stats")
minmoney = cur.fetchone()[0]

from Chapters.MelancholyLib import *

# Logging
logging.basicConfig(filename='logs/FreeRoam.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if debug == True:

    cur.execute("SELECT Weather FROM settings")
    experimental_weather = cur.fetchone()[0]

    cur.execute("SELECT temperature FROM settings")
    experimental_temperature = cur.fetchone()[0]

    print("Debug mode is enabled")
    print("Experimental weather:", experimental_weather)
    print("Experimental temperature:", experimental_temperature)

# Checks Weather

def FreeRoam(season, temperature, location):
    logging.info('FreeRoam started')
    Melancholy.RandomOpening(trauma, Melancholy.forecast_weather(), Melancholy.forecast_temp(), Melancholy.season())
    print(f"I'm at the {location}")
    print(Melancholy.forecast_temp())

FreeRoam(Melancholy.season(), Melancholy.forecast_temp(), location=None)

FreeRoam(Melancholy.season(), Melancholy.forecast_temp(), location=None)
# NOT CURRENTLY FUNCTIONAL