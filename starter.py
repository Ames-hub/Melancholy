import sqlite3
import time
import sys
import random
import logging

# Sets up logging
logging.basicConfig(filename='game.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

health = random.randint(20, 100)
maxhealth = random.randint(20, 100)
maxstamina = random.randint(50, 500)
stamina = random.randint(50, 500)
money = random.randint(2, 20)
sanity = 100 # This value does not need to be corrected
maxsanity = 200 # If it does, it will be corrected in the future
trauma = 100
maxtrauma = 500
corruption = 10

#Corrects the health and maxhealth of the player
def corhealth(maxhealth, health):
    if health > maxhealth:
        health = maxhealth
        return health
    if maxhealth < health:
        maxhealth = health
        return maxhealth

#Corrects the stamina and maxstamina of the player
def corstamina(maxstamina, stamina):
    if stamina > maxstamina:
        stamina = maxstamina
        return stamina
    if maxstamina < stamina:
        maxstamina = stamina
        return maxstamina

#Corrects the money of the player
def cormoney(money):
    if money < 2:
        money = 2 + random.randint(0, 5)
        return money
    if money > 20:
        money = 20
        return money

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

debugdeterminer = input("Debug Passcode... : ")
if debugdeterminer == "Chara":
    debug = True
    print("\033[92m" + "Debug mode enabled" + "\033[0m")
    debugdeterminer = input("Did you mean to enable Debug mode? (y/n) : ")
    if debugdeterminer == "n":
        debug = False
        print("\033[91m" + "Debug mode disabled" + "\033[0m")
    devoptiontypes = input("Do you want to see the types of the variables? (y/n) : ")
    if devoptiontypes == "y":
        devoptiontypes = True
    print("Haha debug mode is enabled meaning something's wrong lol get fucked")
    logging.info("Debug mode = ", debug)
if debugdeterminer == "CHARA":
    # This is the debug mode option for printing data types
    print("Debug mode enabled and all options enabled")
    debug = True
    devoptiontypes = True
    time.sleep(0.600)
    print("Haha debug mode is enabled meaning something's wrong lol get fucked")
    logging.info("Debug mode (Full) = ", debug)
else: 
    debug = False
    devoptiontypes = False
    logging.info("Debug mode = ", debug)

con = sqlite3.connect('game.db')
cur = con.cursor()

timenow = 6
maximumtime = 24

death_message = "You died"
Village_name = "Maple Town"
name = "Change me later but my name is Bob"

if debug == True:
    print("Pre-Correction")
    if devoptiontypes == False:
        print(maxstamina)
    elif devoptiontypes == True:
        print(type(maxstamina), maxstamina)

    if devoptiontypes == False:
        print(stamina)
    elif devoptiontypes == True:
        print(type(stamina), stamina)

    if devoptiontypes == False:
        print(maxhealth)
    elif devoptiontypes == True:
        print(type(maxhealth), maxhealth)
    
    if devoptiontypes == False:
        print(health)
    elif devoptiontypes == True:
        print(type(health), health)
    
    if devoptiontypes == False:
        print(money)
    elif devoptiontypes == True:
        print(type(money), money)

corhealth(maxhealth, health)
corstamina(maxstamina, stamina)
cormoney(money)

if debug == True:
    print("Corrected result...")
    if devoptiontypes == False:
        print(maxstamina)
    elif devoptiontypes == True:
        print(type(maxstamina), maxstamina)

    if devoptiontypes == False:
        print(stamina)
    elif devoptiontypes == True:
        print(type(stamina), stamina)

    if devoptiontypes == False:
        print(maxhealth)
    elif devoptiontypes == True:
        print(type(maxhealth), maxhealth)
    
    if devoptiontypes == False:
        print(health)
    elif devoptiontypes == True:
        print(type(health), health)
    
    if devoptiontypes == False:
        print(money)
    elif devoptiontypes == True:
        print(type(money), money)

# this code is used to create a database for the game
# it contains 3 tables, one for the world, one for the stats and one for developer options

# the world table contains the time, the maximum time, the default death message, the name of the village and the name of the character
# the stats table contains the health, the maxhealth, stamina, maxstamina and money
# the dev table contains dev options, such as debug mode

cur.execute('''CREATE TABLE IF NOT EXISTS World (Time integer PRIMARYKEY, Maximum Time integer, Death Message text, Village Name text, Name text, Progress integer)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Stats (health integer RIMARYKEY, maxhealth integer, stamina integer, maxstamina integer, money integer, Sanity integer, maxsanity integer)''')
cur.execute('''CREATE TABLE IF NOT EXISTS dev (Debug integer PRIMARYKEY)''')
cur.execute('''CREATE TABLE IF NOT EXISTS FirstVisit (Pieeresshop integer PRIMARYKEY, VanishingHospital integer, AdventurersGuild integer)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Special (PieereTherapy integer PRIMARYKEY)''')
cur.execute("INSERT INTO World VALUES (?,?,?,?,?)", (timenow, maximumtime, death_message, Village_name, name))
cur.execute("INSERT INTO Stats VALUES (?, ?, ?, ?, ?, ?, ?)", (health, maxhealth, stamina, maxstamina, money, sanity, maxsanity))
cur.execute("INSERT INTO dev VALUES (?)", (int(debug),))


# Add a ? and a 0 for each location added. This is used to determine if the player has visited the location before. Currently 3 locations
cur.execute("INSERT INTO FirstVisit VALUES (?, ?, ?)", (0, 0, 0))
logging.info("All tables created and values inserted. Success unknown")

con.commit()

# runs the second script using the exec function
#exec(open("Chapters/Chapter1.py").read())