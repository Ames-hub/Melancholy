#imports all the variable's from the table "stats"
import sqlite3
conn = sqlite3.connect('game.db')
c = conn.cursor()
c.execute("SELECT * FROM Stats")
stats = c.fetchall()
gold = stats[0][0]
health = stats[0][1]
stamina = stats[0][2]
#imports all the variables from the table "world"
c.execute("SELECT * FROM world")
world = c.fetchall()
thetime = world[0][0]
maximumtime = world[0][1]
deathmessage = world[0][2]
village_name = world[0][3]
debug = world[0][4]
Name = world[0][5]
#Imports possible exit codes from the table "Exitcodes"

import logging

logging.info ("Chapter1.py has been loaded")