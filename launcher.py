import sqlite3, time, sys, random, logging

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

# Trauma is a experimental value. Its purpose is to make the player feel more vulnerable and less powerful and make the game more challenging.
# and Give the consequences of your actions more weight.
# However, its place in the game is still being decided. It may be removed or changed. 
trauma = 100

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

print("Press ENTER if you are not trying to debug the game")
debugdeterminer = input("Debug Passcode... : ")
if debugdeterminer == "CHARA":
    debug = True
    devoptiontypes = True
else:
    debug = False
    devoptiontypes = False

con = sqlite3.connect('game.db')
cur = con.cursor()
logging.info("Connected to database")

timenow = 6
maximumtime = 24

death_message = "You died"
Village_name = "Maple Town"
name = "Change me later but my name is Bob"

# Defines the chapter in which you are up to
Progress = 0

# the world table contains the time, the maximum time, the default death message, the name of the village and the name of the character
# the stats table contains the health, the maxhealth, stamina, maxstamina and money
# the dev table contains dev options, such as debug mode

cur.execute('''CREATE TABLE IF NOT EXISTS World (Time integer PRIMARYKEY, Maximum Time integer, Death Message text, Village Name text, Progress)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Stats (health integer RIMARYKEY, mingenhealth integer, maxhealth integer, stamina integer, minstamina, maxstamina integer, money integer, minmoney integer, maxgenmoney integer, trauma)''')
cur.execute('''CREATE TABLE IF NOT EXISTS dev (Debug integer PRIMARYKEY)''')
cur.execute('''CREATE TABLE IF NOT EXISTS FirstVisit (Pieeresshop integer PRIMARYKEY, VanishingHospital integer, Therapist integer)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Special (PieereTherapy integer PRIMARYKEY)''')
cur.execute("INSERT INTO World VALUES (?,?,?,?,?)", (timenow, maximumtime, death_message, Village_name, Progress))
cur.execute("INSERT INTO Stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (health, mingenhealth, maxhealth, stamina, minstamina, maxstamina, money, minmoney, maxgenmoney, trauma))
cur.execute("INSERT INTO dev VALUES (?)", (int(debug),))


# Add a ? and a 0 for each location added. This is used to determine if the player has visited the location before. Currently 3 locations
cur.execute("INSERT INTO FirstVisit VALUES (?, ?, ?)", (0, 0, 0))
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
cur.execute("SELECT * FROM FirstVisit")
logging.info("FirstVisit table has data")
cur.execute("SELECT * FROM Special")
logging.info("Special table has data")
logging.info("All tables have data. Success")

con.commit()
logging.info("Committed changes to database")

con.close()

# runs the second script using the exec function
logging.info("Running Chapter 1")
exec(open("Chapters/Chapter1.py").read())