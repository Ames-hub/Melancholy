gamename = 'Melancholy'

import sqlite3, time, sys, random, logging, os
from Chapters.MelancholyLib import *

# Sets up logging
logging.basicConfig(filename='logs/Starter.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

mingenhealth = 20
health = random.randint(20, 100)
maxhealth = 100
minstamina = 50
stamina = random.randint(50, 500)
maxstamina = 500
money = random.randint(2, 20)
minmoney = 0
maxgenmoney = 20

if health > 200:
    health = health // 2

if stamina > 500:
    stamina = stamina // 2

# Trauma is a experimental value. Its purpose is to make the player feel more (or less) vulnerable and less powerful and make the game more challenging.
# and Give the consequences of your actions more weight.
# However, its place in the game is still being decided. It will likely be changed (as it already has been) 
trauma = 100

# I Originally didn't want Trauma to have a limit, but I decided for the purpose of playability, it needs a limit.
# Otherwise, a player could end up in a situation where their trauma is So high, that it isn't practical to reduce it via normal means.
# But, that could happen so I decided to add a limit.
maxtrauma = 2000

print("Press ENTER if you are not trying to debug the game")
debugdeterminer = input("Debug Passcode... : ")
if debugdeterminer == "CHARA":
    debug = True
    devoptiontypes = True
else:
    debug = False
    devoptiontypes = False

gamename = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
con = sqlite3.connect(gamename + ".db")
cur = con.cursor()
logging.info("Connected to database")

timenow = 6
maximumtime = 24

Village_name = "Maple Town"
name = "Change me later but my name is Bob"

# Defines the chapter in which you are up to
Progress = 0

# This asks the player for the settings
# It will be changed to a GUI later
# The settings are stored in the table "Settings" :)

cur.execute('''CREATE TABLE IF NOT EXISTS Settings (Weather integer PRIMARYKEY, Temperature integer)''') # This table needs to be made before the 2 functions below are called

Melancholy.setting("Weather", True, "This will add stuff like Rain, Snow, etc. to Free Roam", con, cur)

Melancholy.setting("Temperature", True, "The temperature system (As of now) only affects\nopenings when you are in free roam", con, cur)

# the world table contains the time, the maximum time, the default death message, the name of the village and the name of the character
# the stats table contains the health, the maxhealth, stamina, maxstamina and money
# the dev table contains dev options, such as debug mode

# SETTING VALUES ARE AUTO-INSERTED BY DEF
cur.execute('''CREATE TABLE IF NOT EXISTS World (Time integer PRIMARYKEY, Maximum Time integer, Village Name text, Progress)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Stats (health integer RIMARYKEY, mingenhealth integer, maxhealth integer, stamina integer, minstamina, maxstamina integer, money integer, minmoney integer, maxgenmoney integer, trauma integer)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Stats2 (maxtrauma integer PRIMARYKEY)''') # Why? because 10 is the limit apparently. :(
cur.execute('''CREATE TABLE IF NOT EXISTS dev (Debug integer PRIMARYKEY)''')
cur.execute("INSERT INTO World VALUES (?,?,?,?)", (timenow, maximumtime, Village_name, Progress))
cur.execute("INSERT INTO Stats2 VALUES (?)", (int(maxtrauma),))
cur.execute("INSERT INTO dev VALUES (?)", (int(debug),))
cur.execute("INSERT INTO Stats VALUES (?,?,?,?,?,?,?,?,?,?)", (health, mingenhealth, maxhealth, stamina, minstamina, maxstamina, money, minmoney, maxgenmoney, trauma))
# Add a ? and a 0 for each location added. This is used to determine if the player has visited the location before. Currently 3 locations
# I really hope there's a better solution to this, but I can't think of one right now.
logging.info("All tables created and values inserted. Success unknown")
logging.info("Checking...")
# Checks if the tables have data in them.
# If they don't, It will throw an error because it cannot fetch.
# If they do, it will log that the tables have data
cur.execute("SELECT * FROM World")
logging.info("World table has data")
cur.execute("SELECT * FROM Stats")
logging.info("Stats table has data")
cur.execute("SELECT * FROM dev")
logging.info("Dev table has data")
logging.info("All tables have data. Success")
logging.info("Committed changes to database")

con.commit()
time.sleep(0.5)
con.close()


# runs the second script using the exec function
logging.info("Running Chapter 1")
exec(open("Chapters/Chapter1.py").read())