import os, time, logging, sys, sqlite3, random
class Melancholy:
    # Clears the console
    def clear():
        os.system('cls' if os.name=='nt' else 'clear')

    def setting(system_name, experimental, description, con, cur):
        Melancholy.clear()
        print(f"Do you want to enable the {system_name} system?")
        if experimental:
          print("            [!] WARNING [!]")
          print("This is an experimental feature and may cause bugs")
        print(description)
        while True:
            act = input("Enable? y/n : ")
            if act == "y":
                returnvalue = True
                cur.execute("INSERT INTO Settings VALUES (?, ?)", (system_name, returnvalue))
                break
            elif act == "n":
                returnvalue = False
                cur.execute("INSERT INTO Settings VALUES (?, ?)", (system_name, returnvalue))
                break

    # THE END MESSAGE INDICATING WHEN THERE IS NO MORE STORY TO BE TOLD
    # custom_git allows you to add your own github link. Enter a STR for it. It will be printed as so
    # https://github.com/customgit
    # Sorry if you have "Debug" in your git link, it will not wait 5 seconds. :(
    def endmsg(gamename, EOL, custom_git=""): 
        if "debug" not in custom_git:
            time.sleep(5)
        Melancholy.clear()

        if EOL == False or EOL == "No" or EOL == "no" or EOL == "NO" or EOL == "n" or EOL == "N":
            print("Sorry! But thats the end of " + gamename + ". I Will continue to develop it :)")
            print("Head over to my Github page if you want to check for updates!")
        else:
            print("Sorry! But that's the end of" + gamename + "\nUnfortunately, This game has reached its EOL and will no longer be updated.")
            print("If you want to see more of my work, check out my github!")
        if custom_git == "":
            print("https://github.com/Ames-Hub")
        else:
            print("https://github.com/" + custom_git)
        print("")
        print("Press CTRL + C to exit")
        time.sleep(10000)
        print("Your still here? Huh.")
        print("Remember, press CTRL + C to exit")
        time.sleep(6)
        print("Or you can just close the window")
        time.sleep(1000)
        print("Seriously, Show's over :(")
        time.sleep(1000)
        print("Why do you have trouble letting go?")
        time.sleep(1000)
        print("A Therapist might suit you.")
        time.sleep(300)
        os.quit("You need help.")

    # Prints a str 1 letter at a time
    def delay_print(s, delay=0.15):
        logging.info("Function 'delay_print' has been called")
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)

    # Prints a str in a certain color
    def print_color(text, color):
        logging.info("Function 'print_color' has been called")
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
        }
        reset = "\033[0m"
        return(f"{colors[color]}{text}{reset}")

    # Prints a str and 1 word in that string as a certain color
    def print_cword(text, word, color):
        logging.info("Function 'print_cword' has been called")
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
        }
        reset = "\033[0m"
        new_text = text.replace(word, f"{colors[color]}{word}{reset}")
        return (new_text)

    # SAVES ALL STATS
    def savestat(trauma, stamina, health, con, cur):
        cur.execute("UPDATE stats SET trauma = ?", (trauma,))
        logging.info("Saved Trauma to DB")
        cur.execute("UPDATE stats SET stamina = ?", (stamina,))
        logging.info("Saved Stamina to DB")
        cur.execute("UPDATE stats SET health = ?", (health,))
        logging.info("Saved Health to DB")
        con.commit()
        logging.info("Saved all stats to DB")

    # Checks health
    def checkhealth(cur):
        # imports health
        cur.execute("SELECT health FROM stats")
        health = cur.fetchone()[0]
        cur.execute("SELECT maxhealth FROM stats")
        maxhealth = cur.fetchone()[0]
        cur.execute("SELECT mingenhealth FROM stats")
        mingenhealth = cur.fetchone()[0]
        logging.info("Health has been checked. Returned as ", health, maxhealth, mingenhealth)
        return health, maxhealth, mingenhealth

    # Checks Stamina
    def checkstamina(cur):
        # Imports stamina
        cur.execute("SELECT stamina FROM stats")
        stamina = cur.fetchone()[0]
        cur.execute("SELECT maxstamina FROM stats")
        maxstamina = cur.fetchone()[0]
        cur.execute("SELECT minstamina FROM stats")
        minstamina = cur.fetchone()[0]
        logging.info("Stamina has been checked. Returned as ", stamina, maxstamina, minstamina)
        return stamina, maxstamina, minstamina

    # GENERIC FUNCTIONS
    # GENERIC FUNCTIONS
    # GENERIC FUNCTIONS

    # Melancholy specific functions
    # Melancholy specific functions
    # Melancholy specific functions

    # ADDS TRAUMA - Melancholy
    def trauma1(trauma):
        print("\033[91m[!] Trauma +\033[0m")
        trauma =+ trauma + 20
        logging.info("Trauma + 20 (trauma1)")
        if trauma < 0:
            trauma = 0
            logging.info("Trauma is less than 0, setting to 0")
    def trauma2(trauma):
        print("\033[91m[!] Trauma ++\033[0m")
        trauma =+ trauma + 50
        logging.info("Trauma + 50 (trauma2)")
        if trauma < 0:
            trauma = 0
            logging.info("Trauma is less than 0, setting to 0")
    def trauma3(trauma):
        print("\033[91m[!] Trauma +++\033[0m")
        trauma =+ trauma + 100 
        logging.info("Trauma + 100 (trauma3)")
        if trauma < 0:
            trauma = 0
            logging.info("Trauma is less than 0, setting to 0")

    # REMOVES TRAUMA - Melancholy
    def trauma1r(trauma):
        print("\033[92m[!] Trauma -\033[0m")
        trauma =+ trauma - 20
        logging.info("Trauma - 20 (trauma1r)")
        if trauma < 0:
            trauma = 0
            logging.info("Trauma is less than 0, setting to 0")
    def trauma2r(trauma):
        print("\033[92m[!] Trauma --\033[0m")
        trauma =+ trauma - 50
        logging.info("Trauma - 50 (trauma2r)")
        if trauma < 0:
            trauma = 0
            logging.info("Trauma is less than 0, setting to 0")
    def trauma3r(trauma):
        print("\033[92m[!] Trauma ---\033[0m")
        trauma =+ trauma - 100 
        logging.info("Trauma - 100 (trauma3r)")
        if trauma < 0:
            trauma = 0
            logging.info("Trauma is less than 0, setting to 0")

    def forecast_weather():

        con = sqlite3.connect(f'{gamename}.db')
        cur = con.cursor()

        # Determines if the experimental_weather system is enabled
        # Determines if the weather system is enabled
        cur.execute("SELECT Weather FROM settings")
        experimental_weather = cur.fetchone()[0]

        if experimental_weather == True:
            temperature = Melancholy.forecast_temp()
            if temperature < 0:
                return "snow"
            elif temperature < 10:
                act = random.randint(1, 15)
                if act > 5 or act < 8:
                    return "rain"
                else:
                    return "cloudy"
            elif temperature > 30:
                return "clear"
            elif temperature > 35:
                return "sunny"
        else:
            return "DISABLED"

    # Checks Temp
    def forecast_temp():

        con = sqlite3.connect(f'{gamename}.db')
        cur = con.cursor()

        '''This function determines the in-game weather'''
        logging.info('forecast def called')

        # Determines if the weather system is enabled
        cur.execute("SELECT temperature FROM settings")
        experimental_temperature = cur.fetchone()[0]

        if experimental_temperature == True:
            act = random.randint(1, 100) + 10
            # if the ACT is low, it'll be a cold af day.
            if act < 25 or act == 25:
                temperature = random.randint(-2, 10)
                if act == 10:
                    temperature = -10
                    logging.info("Rare weather event!", temperature, "c")
            elif act < 30 or act == 30:
                temperature = random.randint(10, 19)
            # If the ACT is medium, it'll be a nice day.
            elif act > 30 and act < 75:
                temperature = random.randint(20, 25)
            # If the ACT is high, it'll be a hot day.
            elif act > 75 or act == 100:
                temperature = random.randint(26, 35)
                act = random.randint(1, 200)
                if act == 25:
                    temperature = random.randint(36, 48)
                    logging.info("Rare weather event!", temperature, "c")
            # Handles the temperature if it's too high or too low
            elif temperature < -10:
                logging.warning("Warning! Temperature is below -10c! This is not normal!")
                temperature = -10
                logging.warning("Temperature has been set to -10c to correct. This is a bug, please report it to the developer!")
            elif temperature > 48:
                logging.warning("Warning! Temperature is above 48c! This is not normal!")
                temperature = 48
                logging.warning("Temperature has been set to 48c to correct. This is a bug, please report it to the developer!")
            return temperature
        else:
            return "DISABLED"

    def season(season=None):
        '''This function determines the in-game season based on the Hour'''
        logging.info('season def called')
        hour = time.strftime("%H")
        # Progresses the seasons as they would IRL (eg, Spring > Summer > Fall > Winter) to prevent only seeing 1 season
        if random.randint(1, 10) >= 3:
            if hour < 9:
                if season == "Spring":
                    return "Summer"
                else:
                    return "Summer"
            elif hour < 12:
                if season == "Summer":
                    return "Fall"
                else:
                    return "Fall"
            elif hour < 0:
                if season == "Fall":
                    return "Winter"
                else:
                    return "Fall"
            elif hour < 5:
                if season == "Winter":
                    return "Spring"
        else:
            act = random.randint(1, 4)
            if act == 1:
                return "Spring"
            elif act == 2:
                return "Summer"
            elif act == 3:
                return "Fall"
            elif act == 4:
                return "Winter"

    # Prints a random opening depending on env var's everytime its called
    def RandomOpening(trauma):

        debug = True

        # Imports debug from the DB
        con = sqlite3.connect(f'{gamename}.db')
        cur = con.cursor()
        cur.execute("SELECT debug FROM dev")
        debug = cur.fetchone()[0]

        logging.info('RandomOpening def called.', 'debug = ', debug)
        act = random.randint(1, 3)
        # WEATHER RESPONSES
        # COLD WEATHER

        temperature = Melancholy.forecast_temp()
        weather = Melancholy.forecast_weather()

        print("Act: ", act)

        # act = 1 # Debug act

        if act == 1:
            if debug == True:
                # Prints temperature if true
                print("Debug: Temperature is", temperature, "c")
                print("Debug: Weather is", weather)
            if temperature < 18:
                # Responses For temperature being below 18
                print("I walk around the city, a cool breeze flows by. Brr!")
                if weather == "snow":
                    logging.warning("Weather: SNOW is true and temperature is above 0c")
                if weather == "cloudy":
                    print("The sky is cloudy, I hope it doesn't rain...")
                if weather == "rain":
                    # Responses For temperature being below 18 and raining
                    abc = random.randint(1, 2)
                    if abc == 3:
                        print("Its raining and cold, Just my luck...")
                    if abc == 2:
                        print("Its raining and chilly, I should probably get an umbrella...")
                    if abc == 1:
                        print("Its pouring down. Guess I'll stay under shelter as I go")
                if weather == "clear":
                    print("The sky is clear!")
                    # Remember to add a Time flow system! If it is night, make it also say "I can see the stars!"
            elif temperature < 8:
                print("Looking at this weather, I should have brought a jacket...")
                if weather == "snow":
                    print("Its snowing, I should get home soon")
                elif weather == "cloudy":
                    print("The sky is cloudy, I hope it doesn't rain...")
                elif weather == "rain":
                    print("Its raining, I should might get an umbrella...")
                elif weather == "clear":
                    print("The sky is clear, surpringly")

            elif temperature < 0 or temperature == 0:
                print("So cold! The water is freezing up, Do I really need to be out here? Can't it all wait?")
                time.sleep(3)
                print("I guess I'll just have to tough it out...")
                if weather == "snow":
                    print("Its snowing, its cold, P a i n .")

            # NEUTRAL WEATHER
            elif temperature > 18:
                print("I walk around the city, a nice breeze blows by, the leaves rustle in the wind and sunshine beam's through the buildings")
                if weather == "cloudy":
                    print("The sky is cloudy, It'd suck if it rained. Ruins my hair and an alright day like this...")
                elif weather == "rain":
                    print("Ah. rain, how lovely.")
                elif weather == "clear":
                    print("A Nice and clear day too!")
            elif temperature > 23:
                # UT REFERENCE? :OO
                print("I walk around the city, it's a beautiful day outside. Flower's are blooming, Bird's are chirping... Perfect day for a game of Catch!")
                abc = random.randint(1, 100)
                if abc == 50:
                    print("I don't know why, but I have a feeling someone would say")
                    Melancholy.delay_print("Its a beautiful day outside... Birds are singing... Flowers are blooming... On days like these, kids like you... S h o u l d   b e   b u r n i n g   i n   h e l l .")
                    if weather == "cloudy":
                        print("Sure are a lot of clouds, fingers crossed for no rain!")
                    elif weather == "rain":
                        Melancholy.delay_print("P e r f e c t . Rain, on such a nice day")
                    elif weather == "clear":
                        print("A Nice and clear day too!")
            # HOT WEATHER
            elif temperature > 30:
                print("I walk around the city, it's a beautiful day outside. The sun is shining, a bit too hot for my liking... the air is warm.")
                print("I can't wait to get home and take a nice cool shower!")
                if weather == "sunny":
                    print("Sun is rather glaringly bright today though")
                elif weather == "clear":
                    print("At least there's not much glare from the sun")
                elif weather == "cloudy":
                    print("Some clouds, Some rain would be nice on a day like this")
            elif temperature > 1000:
                for i in range(1000): 
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        if act == 2:
            # Random comments on the environment
            abc = random.randint(1, 5)
            if abc == 1:
                print("Some kids are playing in the playground.. I wish I could play with them...")
            elif abc == 2:
                print("The city looks so clean today.. They should pay the cleaners more")
            elif abc == 3:
                print("2 people are yelling at each other in the park...")
                time.sleep(3)
                print("One is dressed in a clean suit and the other in a mechanic's suit.")
                time.sleep(3)
                print("Its none of my business...")
                cba = random.randint(1, 200)
                if cba == 60:
                    print("As I start to look away, I'm drawn back in by the sound of screams...")
                    time.sleep(3)
                    print("The man in the clean suit stabbed the mechanic")
                    Melancholy.trauma3(trauma)
                    time.sleep(3)
                    print("I run as quickly as I can")
            elif abc == 4:
                print("An angry man in a clean business suit is waiting impatiently outside a building")
                print("Its not my business.")
            elif abc == 5:  
                print("The coloured glass looks nice with the sun rays shining through it")
                print("I wonder what it would look like if it was raining...")
        if act == 3:
            # Random thoughts
            abc = random.randint(1, 3)
            if abc == 1:
                print("Is the ocean a soup?")
                time.sleep(2)
                if weather == "rain":
                    print("... Is rain a soup?")
            elif abc == 2:
                print("I wonder what it would be like to be a fish...")
            elif abc == 3:
                print("Can a fish cry?")

gamename = 'Melancholy'

import sqlite3, time, sys, random, logging, os



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

timenow = 6
maximumtime = 24

Village_name = "Maple Town"
name = "Change me later but my name is Bob"

# Defines the chapter in which you are up to
Progress = 0

# This asks the player for the settings
# It will be changed to a GUI later
# The settings are stored in the table "Settings" :)

def os_clear():
    os.system('cls' if os.name=='nt' else 'clear')

def setting(system_name, experimental, description):
    con = sqlite3.connect(f"{gamename}.db")
    cur = con.cursor()
    os_clear()
    print(f"Do you want to enable the {system_name} system?")
    if experimental:
      print("            [!] WARNING [!]")
      print("This is an experimental feature and may cause bugs")
    print(description)
    while True:
        act = input("Enable? y/n : ")
        if act == "y":
            returnvalue = True
            cur.execute("INSERT INTO Settings VALUES (?, ?)", (system_name, returnvalue))
            break
        elif act == "n":
            returnvalue = False
            cur.execute("INSERT INTO Settings VALUES (?, ?)", (system_name, returnvalue))
            break

setting("Weather", True, "This will add stuff like Rain, Snow, etc. to Free Roam")

setting("Temperature", True, "The temperature system (As of now) only affects\nopenings when you are in free roam")

# the world table contains the time, the maximum time, the default death message, the name of the village and the name of the character
# the stats table contains the health, the maxhealth, stamina, maxstamina and money
# the dev table contains dev options, such as debug mode

# SETTING VALUES ARE AUTO-INSERTED BY DEF
con = sqlite3.connect(f"{gamename}.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Settings (Weather integer PRIMARYKEY, Temperature integer)''') # This table needs to be made before the 2 functions below are called
cur.execute('''CREATE TABLE IF NOT EXISTS World (Time integer PRIMARYKEY, Maximum Time integer, Village Name text, Progress)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Stats (health integer RIMARYKEY, mingenhealth integer, maxhealth integer, stamina integer, minstamina, maxstamina integer, money integer, minmoney integer, maxgenmoney integer, trauma integer)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Stats2 (maxtrauma integer PRIMARYKEY)''') # Why? because 10 is the limit apparently. :(
cur.execute('''CREATE TABLE IF NOT EXISTS dev (Debug integer PRIMARYKEY)''')
con.commit()
cur.execute("INSERT INTO World VALUES (?,?,?,?)", (timenow, maximumtime, Village_name, Progress))
cur.execute("INSERT INTO Stats2 VALUES (?)", (int(maxtrauma),))
cur.execute("INSERT INTO dev VALUES (?)", (int(debug),))
cur.execute("INSERT INTO Stats VALUES (?,?,?,?,?,?,?,?,?,?)", (health, mingenhealth, maxhealth, stamina, minstamina, maxstamina, money, minmoney, maxgenmoney, trauma))
con.commit()
con.close()

# CHAPTER 1.0
# This is the first chapter of the game, it is the tutorial chapter
# Chapter 1.0 Is the story of the character's either peaceful exit or escape from the hospital
# Both routes teach the same components, but the easier route is the peaceful route.

import logging, time, sqlite3

# Sets up logging
logging.basicConfig(filename='logs/Chapter1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sets up logging to put all errors in logs/Errors.log
logging.basicConfig(filename='logs/error.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()

con = sqlite3.connect(f'{gamename}.db')
cur = con.cursor()
logging.info("Connected to database")

logging.info ("Chapter1.py has been loaded")

# Imports trauma from the DB
cur.execute("SELECT trauma FROM Stats")
trauma = cur.fetchone()[0]
logging.info("Trauma imported from DB")
# Imports trauma from the DB
# Imports Stamina from the DB
cur.execute("SELECT stamina FROM Stats")
stamina = cur.fetchone()[0]
logging.info("Stamina imported from DB")
# Imports Stamina from the DB
# Imports Health from the DB
cur.execute("SELECT health FROM Stats")
health = cur.fetchone()[0]
logging.info("Health imported from DB")
# Imports Health from the DB
# Imports progress from the DB
# Imports progress from the DB
cur.execute("SELECT Progress FROM world")
progress = cur.fetchone()[0]
logging.info("Progress imported from DB")
# Makes a table called MetHazel with 1 column called Met (0 = False, 1 = True)
cur.execute("CREATE TABLE IF NOT EXISTS MetHazel (Met INT)")
logging.info("Created table 'MetHazel'")

#########################################################################
#                                                                       #
#   This is the first chapter of the game, it is the tutorial chapter   #
#                                                                       #
#########################################################################

print("Welcome to Melancholy!")
time.sleep(1)
print("This is a text based adventure game, where you will be able to make choices that will affect the story.")
time.sleep(1)
print("Eventually, I will figure out how I add a GUI but for the meanwhile, we'll have to make this work.")
time.sleep(1)
print("Please only answer with answers that are offered or with Yes or No.")
print("")
print("You'll want to write these stats down")
print(stamina, "This number is your Stamina. 500 is the Maximum")
print(health, "This number is your Health. 100 is the Maximum")
print("")

Continue = input("Ready? : ")
time.sleep(1)
if "Yes" or "yes" or "Y" or "y" in Continue:
    Melancholy.clear()
    print("Great!")
    time.sleep(1)
    print("Now, let's get started!")
    time.sleep(2)
    for i in range(50):
        print("...")
elif "No" or "no" or "N" or "n" in Continue:
    print("Well, too bad. We're starting anyway.")
    time.sleep(2)
    for i in range(50):
        print("...")
else:
    print("Well, SOMEONE wasn't paying attention >:(")
    exit(logging.error("User did not respond with Yes or No"))

# The entirety of Chapter 1.0
def Chapter1(trauma, stamina, health, progress):
    #######################################
    # THIS IS AN EXAMPLE OF DETECTIVE WORK#
    #######################################
    print("I wake up in a hospital bed.")
    time.sleep(3)
    print("I think to yourself...")
    time.sleep(3)
    print("What happened?")
    time.sleep(3)
    print("I immediately notice I can't see out of my left eye.")
    time.sleep(2)
    act = input("Thats.. Scary.. should I check my eye?... : ")
    if "Yes" in act or "yes" in act or "Y" in act or "y" in act:
        print("I touch where I think my eye is...")
        time.sleep(2)
        print("I feel a bandage, I feel around my head and I notice its wrapped around my head.")
        time.sleep(4)
        print("I look at the mirror to my left, it definitely a bandage.")
        time.sleep(3)
        print("What happened?")
        time.sleep(3)
    time.sleep(4)
    print("I look around the room.\nA cool and sterile room. The blinding sun shines through the window...")
    time.sleep(3)
    print("I look at your hands. They are covered in bandages.")
    time.sleep(3)
    print("I look at the IV Drip... It's half full, Looks clean.")
    time.sleep(3)
    print("")
    print("[!] Some ACTIONS may require detective work.\nThis is not normally complicated.")
    act = input("I think I'm in a... : ") 
    # Rewrite the couple of "Acts" below to less cringe.
    if "Hospital" in act or "Clinic" in act or "infirmary" in act or "ER" in act or "Emergency Room" in act:
        logging.info ("User answered the ACT question (act1) answer: " + act)
        time.sleep(1)
        print("It looks close enough to one at least.")
        a = 1
        time.sleep(3)
        print("You look around the room, trying to remember what happened.")
        time.sleep(3)
        print("")
        print("Options: Concerning or Ok")
        act = input("I don't remember much... that's... : ")
        logging.info ("User answered the ACT question (act2) answer: " + act)
        if "Scary" in act or "Concerning" in act or "Terrifying" in act or "Frightening" in act or "Worrying" in act:
            time.sleep(3)
            print("")
            print("'Wh..What's happening?? Why can't I remember anything?! What's going on?!\n I need to get out of here!'")
            Melancholy.trauma1(trauma)
            time.sleep(3)
            print("I try to get out of the bed, but I am immediately pulled back.\nYou immediately notice the IV Drip, Its tangled up around the Bed frame and restraining you.")
            time.sleep(5)
            print("I try to pull it off, but it's too tight. I can't get it off! ")
            Melancholy.trauma1(trauma)
            time.sleep(2)
            print("A group of people in clean white suits rushes in, They're going to kill me!")
            print("[!] Stamina check")
            if stamina > 400:
                print("I Struggle against the IV Drip's cable again, I can see it buckle under my persistance.")
                time.sleep(1)
                print("With another hard pull, It breaks apart and I'm free!")
                # Initiates the Escape route
                logging.info("User has initiated 'escaping the hospital! (vChapter1))'")
                # Here will open another py file that will lead to the esc route
                EscChapter1(trauma, health, progress, stamina)
                #exec(open("Chapters/EscChapter1.py").read())
                exit()
            elif stamina < 400:
                Melancholy.print_cword("I struggle against the IV Drip cable, it doesn't budge", "it doesn't budge", "red") 
                time.sleep(2)
                print("'Hold them down! They're trying to escape!'\nThey say as they push me down and")
                s = "And..."
                Melancholy.delay_print(s)
                print("...")
                s = 'inject.. Something...'
                Melancholy.delay_print(s)
                IVStamCheckFail(health, stamina, trauma, progress, panicked=True)
        elif 'ok' in act or 'Ok' in act or 'Okay' in act or 'Okay' in act or "Fine" in act or "fine" in act:
            print("Whatever, its fine... its not what matters right now")
            time.sleep(2)
            print("I need to stay Calm, I'm sure everything will be explained soon enough.")
            time.sleep(3)
            print("I try to get out of the bed and stand up, But I'm pulled back by the IV drip. Its a bit tangled up")
            time.sleep(3)
            Melancholy.print_cword("I try to untangle it, but its not possible from where I am.", "not possible from where I am.", "red")
            time.sleep(3)
            print("How did this even happen? IV drip's don't tangle themselves. Not that badly")
            time.sleep(5)
            print("The door opens up and a blonde woman walks in. They're holding a clipboard.")
            time.sleep(3)
            IVStamCheckFail(health, stamina, trauma, progress, panicked=False)
        else:
            print("Come on, Play along now.")
            print("In the future chapters, there will be loops to \nprevent game exit on a invalid choice")
            print("But for now, play along.")
    # User gets the ACT wrong and they get traumatized.
    elif "Hospital" not in act or "Clinic" not in act or "infirmary" not in act or "ER" not in act or "Emergency Room" not in act:
        time.sleep(3)
        logging.info("User failed to answer the ACT question (act1)")
        Melancholy.print_cword("That... somehow doesn't sound right", "somehow doesn't sound right", "red")
        time.sleep(1)
        print("This is so confusing... Where am I?")
        time.sleep(2)
        print("The sun is shining brightly, it shifts through the window and blinds you for a moment.")
        time.sleep(3)
        print("You look around the room, trying to remember what happened, What happened!?")
        time.sleep(3)
        print("Why can't I see out my right eye?!")
        time.sleep(2)
        print("Why are there bandages on my hands?!")
        Melancholy.trauma2(trauma)
        time.sleep(2)
        print("Wait... I can't remember anything, Where's my memory!? What's happening!")
        Melancholy.trauma1(trauma)
        time.sleep(3)
        print("I try to get out of the bed, but I am immediately pulled back.\nYou immediately notice the IV Drip, Its tangled up around the Bed frame and restraining you.")
        if stamina > 400:
            print("I Struggle against the IV Drip's cable again, I can see it buckle under my persistance.")
            time.sleep(1)
            print("With another hard pull, It breaks apart and I'm free!")
            # Initiates the Escape route
            logging.info("User has initiated 'escaping the hospital! (vChapter1))'")
            # Here will open another py file that will lead to the esc route
            EscChapter1(trauma, health, progress, stamina)
            #exec(open("Chapters/EscChapter1.py").read())
            exit()
        else:
            time.sleep(5)
            print("I try to pull it off, but it's too tight. I can't get it off! ")
            Melancholy.trauma1(trauma)
            time.sleep(2)
            print("A group of people in clean white suits rushes in, Why are they here!?")
            time.sleep(2)
            print("'Hold them down! They're trying to escape!'\nThey say as they push me down and")
            s = "and..."
            Melancholy.delay_print(s)
            print("...")
            s = 'inject.. Something...'
            Melancholy.trauma1(trauma)
            Melancholy.delay_print(s)
            # Updates the Progress in World to be "FailedEsc"
            progress = "FailedEsc"
            cur.execute("UPDATE world SET Progress = ?", (progress,))

def EscChapter1(trauma, stamina, health, progress, con, cur):
    print("You dash out of the hospital door, Shoving away anyone in the way")
    time.sleep(3)
    print("You run down the corridor, Following the emergency exit signs.")
    time.sleep(3)
    print("Suddenly, you hear an announcement from the PA System")
    time.sleep(3)
    print("In a monotone voice, They say")
    time.sleep(2.5)
    Melancholy.delay_print('"Attention all staff, a code amber has been declared for 112."')
    time.sleep(2)
    x = False
    while x == False:
        print("You encounter a fork in the hallway.")
        time.sleep(2)
        # Detective work is possible here
        print("The security moniter blinks between sections")
        time.sleep(3)
        print("You hear 4 adult's. on the right side of the Fork in the hallway. They seem panicked.")
        time.sleep(3)
        print("You hear the sound of a child playing and 2 adults talking on the left side.")
        time.sleep(3)
        print("Okay, I can go either left or right...")
        time.sleep(2)
        print("")
        print("[!] This is an example of 'Hidden detective work' In this scenario\nThere is something you can say to get a more controllable result.\nIt is hinted at in this scenario")
        print("You will not get this 'callout' while outside of the tutorial. It is only here now to show you what it is like.")
        print("")
        act = input("I'll... ")
        if "Left" in act or "Right" in act or "left" in act or "right" in act:
            break
        if "moniter" in act or "security" in act:
            print("You look at the security moniter, It's a bit blurry, but you can make out the people on the screen.")
            time.sleep(5)
            print("You see 4 adults on panel 1. They are dressed in Hospital security uniforms. They're organizing locking down the hospital entrances.")
            time.sleep(5)
            print("You see 1 of them scanning through the CCTV footage, They seem to be looking for you.")
            time.sleep(5)
            print("You look around you, You see a CCTV Camera on the ceiling. Its not looking at you now, but it definitely saw you before")
            Melancholy.trauma1(trauma)
            print("These people must be on the \033[33mRight\033[0m side of the hallway")
            time.sleep(5)
            print("You see 2 adults on panel 2. They are talking to each other, You can't make out what they're saying.")
            time.sleep(3)
            print("They look at a toddler and quickly stop them from pulling out an outlet")
            time.sleep(3)
            print("They must be the parents of the child you heard earlier.")
            print("These people must be on the \033[33mLeft\033[0m side of the hallway")
            input("Press enter to continue...")
            # Breaks the operation when the user enters "left" or "right" in the string variable ACT
            # Keeps looping using the "While" Statement until the user enters "left" or "right"
            # This branch-off of is a result of the user entering "moniter" or "security" in the string variable ACT

        if "left" in act or "Left" in act:
            print("You dash down the left hallway.")
            time.sleep(3)
            print("As you run down the hallway, A hand grabs your shoulder and pulls you back.")
            time.sleep(3)
            print("You turn around to see a tall, strong man dressed in casual clothing.")
            time.sleep(3)
            print("They get down on their knee to look you in the eye and say")
            Melancholy.delay_print("'Woah champ, slow down! You're going to hurt yourself!'")
            time.sleep(3)
            if trauma > 300:
                # Prints in red "You look at the man, stunned with fear"
                Melancholy.print_color("You look at the man, stunned with fear", "red")
                print("")
                print("[!] Trauma")
                print("having too high trauma takes control from you in certain situations")
                print("It can have you make bad or good decisions. Normally, they are bad.")
                print("")
                input("Press enter to continue")
                time.sleep(2)
                print("'I don't want to die!' You think to yourself")
                time.sleep(2)
                print("'Now now, Everything is going to be alright' The tall man says")
                time.sleep(2)
                Melancholy.trauma3r(trauma)
                Melancholy.print_cword("Their voice is oddly calming", "calming", "blue")
                time.sleep(3)
                Melancholy.print_cword("You must be why they called a amber alert", "amber alert", "yellow")
                time.sleep(3)
                print("Do not worry, I do not know why you chose to ran. but I will not let them harm you.")
                time.sleep(5)
                Melancholy.trauma2r(trauma)
                # Create's a new table called "TallStrongProt"
                cur.execute('''CREATE TABLE IF NOT EXISTS TallStrongProt (TSP integer PRIMARYKEY)''')
                TSP = 1
                cur.execute("INSERT INTO TallStrongProt VALUES (?)", (int(TSP),))
                con.commit
                Melancholy.savestat(stamina, trauma, health)
                print("'The exit is down here' The man says, pointing down the hallway")
                time.sleep(5)
                print("You give them a hug")
            else:
                print("You smile apologetically at the man")
                time.sleep(3)
                print("'You shouldn't run indoors, I'm sure you're parents have told you thi-'")
                time.sleep(3)
                print("They look at my Hospital clothes as if they realized something")
                time.sleep(2)
                print("I hope they didn't...")
                time.sleep(3)
                Melancholy.print_cword("'Ah. So your why they declared a code amber", "code amber", "yellow")
                time.sleep(3)
                print("'disregarding running in the hallway, You should especially not run from doctors!'")
                time.sleep(3)
                print("'I understand the desire to, But they're here to help and to keep you alive'")
                time.sleep(3)
                print("'Now, Lets get you back.'")
                time.sleep(3)
                print("")
                print("Options: Run or Follow\nRunning will finish the escape scene\nFollowing will continue the hopsital story")
                print("")
                act = input("They're about to bring me back to the doctors! I... ")
                if "Run" in act or "run" in act or "struggle" in act or "Struggle" in act:
                    print("[!] Stamina check")
                    if stamina > 405:
                        print("I tug suddenly, surprising them! They stumble")
                        time.sleep(2)
                        print("I run as fast as I can down the hallway, I see the exit sign!")
                        time.sleep(2)
                        print("The guard's are distracted by angry people wanting to leave, I sneak past them and escape!")
                        logging.info("Chapter 1.0 completed! (ESCAPE ROUTE) initialising Chapter 1.1")
                        #cur.execute('''CREATE TABLE IF NOT EXISTS Chapt1End (End text PRIMARYKEY)''')
                        #ending = "Escaped hospital! (Right hall)"
                        #cur.execute("INSERT INTO Chapt1End VALUES (?)", (str(ending),))
                        Melancholy.savestat(stamina, trauma, health)
                        Chapter1_1(health, trauma, stamina, progress)
                        #exec(open("Chapters/Chapter2.py").read())
                    else:
                        logging.info("Failed Escape Route")
                        print("They pick you up and call out to... Their wife?")
                        time.sleep(5)
                        print("'Honey, I'm going to go return this patient to the doctor's.'")
                        time.sleep(3)
                        print("'Watch the child while I'm gone please!'")
                        time.sleep(4)
                        print("She replies 'Who'd have thought we'd find them? Sure, I'll watch them while your gone.'")
                        time.sleep(3)
                        print("They carry you in their arms back to the doctor")
                        time.sleep(3)
                        print("You pass several people on the way there.")
                        time.sleep(3)
                        Melancholy.print_cword("You feel a sudden wave of Exhaustion...", "Exhaustion", "blue")
                        Melancholy.delay_print("You fall asleep...")
                        Melancholy.savestat(stamina, trauma, health)
                        IVStamCheckFail(trauma, health, stamina, progress, panicked=True)
                elif "Follow" in act or "follow" in act or "Stay calm" in act or "stay calm" in act:
                    logging.info("Decided to Fail Escape Route")
                    print("They pick you up and call out to... Their wife?")
                    time.sleep(5)
                    print("'Honey, I'm going to go return this patient to the doctor's.'")
                    time.sleep(3)
                    print("'Watch the child while I'm gone please!'")
                    time.sleep(4)
                    print("She replies 'Who'd have thought we'd find them? Sure, I'll watch them while your gone.'")
                    time.sleep(3)
                    print("They carry you in their arms back to the doctor")
                    time.sleep(3)
                    print("You pass several people on the way there.")
                    time.sleep(3)
                    Melancholy.print_cword("You feel a sudden wave of Exhaustion...", "Exhaustion", "blue")
                    Melancholy.delay_print("You fall asleep...")
                    Melancholy.savestat(stamina, trauma, health)
                    IVStamCheckFail(trauma, health, stamina, progress, panicked=True)
        # THIS IS CORRECTLY INDENDTED DONT FUCKING CHANGE IT
        # This is the path where the player encounter's guards when turning right
        elif "right" in act or "Right" in act:
            print("I run to the right hallway.")
            time.sleep(5)
            print("I turn the corner and see 4 guards walking my way, They haven't seen me yet! What do I do?!")
            Melancholy.trauma1(trauma)
            time.sleep(3)
            print("")
            print("[!] Detective work is possible here, but not required")
            print("")
            time.sleep(3)
            print("Ok calm down, Think...")
            time.sleep(2)
            print("There's a cleaning closet to my right, I could hide in there!")
            Melancholy.print_cword("Option: Hide", "Hide", "blue")
            time.sleep(4)
            print("Or I could run down the hallway past the guards and try to escape!")
            Melancholy.print_cword("Option: Run", "Run", "Red")
            time.sleep(3)
            act = input("I... ")
            if "Hide" in act or "hide" in act:
                print("I run to the closet and I open the door and close it behind me")
                time.sleep(2)
                print("I slowly close it to keep quiet and I wait for the security to pass")
                time.sleep(2)
                print("I hear footsteps getting closer and closer")
                Melancholy.trauma1(trauma)
            elif "Run" in act or "run" in act:
                print("I run down the hallway as fast as I can!")
                time.sleep(2.5)
                print("The security guards look at me running past them, A couple try to grab me but I barely move out of the way")
                Melancholy.trauma1(trauma)
                time.sleep(2.5)
                print("2 of the guard's yell 'HALT!' and start running towards me while the other 2 run around the corner")
                time.sleep(2.5)
                print("They yell, 'Damnit, Slow down! We aren't gonna hurt you!'")
                time.sleep(2.5)
                print("One of the guard's stumble, They fall down and hit their head, Dazing them")
                time.sleep(2.5)
                print("The other one however, They are gaining on me!")
                Melancholy.trauma1(trauma)
                time.sleep(2.5)
                Melancholy.print_cword("I run as fast as I can, but they catch me", "but they catch me", "red")
                time.sleep(2.5)
                print("They grab me from behind and pull me up by my arms until my feet don't touch the floor")
                time.sleep(3.5)
                print("[!] Stamina check")
                if stamina > 440:
                    print("with all my strength, I raise my legs up to their face and kick them")
                    Melancholy.print_color("Stamina -", "red")
                    stamina =- 20
                    Melancholy.savestat(stamina, trauma, health)
                    print("They stumble and I run towards the exit, I open the door and dash out")
                    time.sleep(5)
                    print("I kept running for what felt like days")
                    time.sleep(3)
                    Melancholy.delay_print("I eventually... passed... out...")
                    logging.info("Chapter 1.0 Completed. Running 1.1")
                    Chapter1_1(health, trauma, stamina, progress)
                else:
                    print("With all my strength, I raise my legs up to their face and kick them")
                    time.sleep(3)
                    print("They move out of the way, and then restrain my legs")
                    time.sleep(4)
                    print("'Woah, Your not happy are you! We're not gonna hurt you, just calm down!' They say with a slight annoyance in their voice")
                    time.sleep(2)
                    print("I've gotta get out!")
                    time.sleep(3)
                    print("I keep trying to kick them, they keep dodging")
                    time.sleep(3)
                    print("'Ah bloody hell' They grab a pill and force you to swallow it")
                    time.sleep(2.5)
                    print("You feel a sudden wave of exhaustion...")
                    time.sleep(2.5)
                    Melancholy.delay_print("You fall asleep...")
                    logging.info("User sent to IVStamCheckFail")
                    IVStamCheckFail(stamina, health, trauma, progress)

def Chapter1_1(trauma, stamina, health, progress):
    print("wow")
    Melancholy.savestat(stamina, trauma, health)
    Melancholy.endmsg(gamename=gamename, EOL=False)


# The end for if the user did not have the stamina to escape the Tangled up IV cord
def IVStamCheckFail(trauma, health, stamina, progress, panicked):

    # Inserts into the DB that Hazel was met.
    cur.execute("INSERT INTO MetHazel VALUES (?)", (int(1),))

    if panicked == True:
        time.sleep(4)
        Melancholy.clear()
        Melancholy.savestat(stamina, trauma, health, con, cur)
        Melancholy.delay_print("You wake up... You feel tired and dazed")
        time.sleep(3)
        print("...")
        Melancholy.delay_print("A Doctor stands next to you.. Is that who that was?")
        time.sleep(2)
        print("...")
        print("It must have been...")
        time.sleep(2)
        print(...)
        print("'hm?' The doctor says, They glance down at you")
        time.sleep(4)
        print("'Ah, your awake!' She says as she puts down her notepad")
        time.sleep(4)
        print("'Don't go running off on us again okay?' They chuckle")
        time.sleep(4)
        print("Will you reply assuring you wont (A: Wont)\nor will you say you will run off (A: will)")
        act = input("I... ")
        if "Wont" in act or "wont" in act or "won't" in act or "Won't" in act or "will" in act or "Will" in act:
            Melancholy.delay_print("I shake my head")
            if "will" in act or "Will" in act:
                print("No... I won't do that again")
            print("...")
            time.sleep(3)
            print("'You won't? Good, I'm glad to hear that.' She says")
            time.sleep(4)
            print("'Now, I'm going to ask you a few questions, and I want you to answer them honestly.'")
            time.sleep(4)
            print("'Do you know your name?'")
            time.sleep(4)
            print("'...'")
            time.sleep(2)
            print("'You aren't one for conversation are you?' She says with a slight smile")
            time.sleep(4)
            print("'Well that's alright, I'll just have to ask you some more questions.'")
            time.sleep(4)
            print("'Do you know where you are?'")
            act = input("I am are in a... ")
            if "Hospital" in act or "Clinic" in act or "infirmary" in act or "ER" in act or "Emergency Room" in act:
                time.sleep(2)
                print("You think back to when you woke up... you were in a Medical institution.")
                time.sleep(2)
                act = input("Do you answer honestly? (A: Yes) or (A: No) : ")
                if "Yes" in act or "Y" in act:
                    print("You nod your head and smile")
                    time.sleep(4)
                    print("'Yes, you are in a Hospital!' She says as she writes down your answer")
                    time.sleep(4)
                if "No" in act or "N" in act:
                    print("You shake your head and look at them with a slight frown")
                    time.sleep(4)
                    print("'Oh, I see..' She says as she writes down your answer, returning a slight frown")
                    time.sleep(4)
                    print("'Well, your in a Hospital'")
                    time.sleep(2)
            else:
                time.sleep(2)
                Melancholy.print_cword("You think back to when you woke up... you didn't know where you were. [Trauma]", "[Trauma]", "red")
                time.sleep(3)
                act = input("Do you answer honestly? (A: Yes) or (A: No) : ")
                if "Yes" in act or "Y" in act:
                    print("You nod your head and smile")
                    time.sleep(4)
                    print("'Yes, you are in a Hospital!' She says as she writes down your answer")
                    time.sleep(4)
                if "No" in act or "N" in act:
                    print("You shake your head and look at them with a slight frown")
                    time.sleep(4)
                    print("'Oh, I see..' She says as she writes down your answer, returning a slight frown")
                    time.sleep(4)
                    print("'Well, your in a Hospital'")
                    time.sleep(2)
            print("'Now, Do you know what happened to you?'")
            time.sleep(3)
            print("'Or rather, what happened to make you need to come here?'")
            time.sleep(4)
            print("I try to think back, but I can't remember anything relevant.")
            time.sleep(4)
            print("I was walking down a lonely street with some friends, and then I woke up here.")
            time.sleep(4)
            print("I shake my head")
            time.sleep(3)
            print("'Well, that's alright. We can determine it with the help of modern technology.' She says")
            time.sleep(4)
            print("'Your Injuries were quite extensive.'")
            Melancholy.trauma1(trauma)
            time.sleep(2)
            print("'Now now, Don't worry about that. You're safe now. I wont let anyone hurt you.'")
            time.sleep(4)
            print("Their voice is soothing, You feel better.")
            time.sleep(1)
            Melancholy.trauma3r(trauma)
            print("")
            print("[!] Theraputic actions")
            print("Theraputic actions are actions that help you recover from trauma.")
            print("You can hire or randomly encounter these actions.")
            print("Lower trauma levels will help you have more control over your environment.")
            print("You can only check your trauma level by checking at the Therapists.")
            print("")
            a = input("Press enter to continue")
            print("")
            print("The door closes and the doctor says 'I'm back!'")
            time.sleep(3)
            print("You didn't even notice them leave?")
            time.sleep(3)
            print("You wave at them and smile")
            time.sleep(4)
            print("A Face of annoyance appears on their face 'Oh who did this to you?' They say")
            time.sleep(3)
            print("You look at them with a hint of fear as they get closer..")
            time.sleep(1)
            print("But why? They have only been kind..")
            time.sleep(5)
            print("They grab the IV Drip tangled around your sleeve and carefully take it off")
            Melancholy.trauma1r(trauma)
            time.sleep(3)
            print("They look at you with a smile and say 'There we go!~'")
            time.sleep(2)
            print("She gets close enough for you to be able to read their nametag")
            time.sleep(2)
            print("It says 'Dr. Hazel Locklin' on it")
            time.sleep(4)
            print("You smile at Hazel")
            time.sleep(2)
            print("'You're welcome!' She says as they put the IV Drip in a nearby trash can")
            time.sleep(3)
            print("'You won't be needing this anymore' She says")
            time.sleep(3)
            print("They sit down next to you and say 'So, what's your name?'")
            time.sleep(3)
            print("'Ah, I'm sorry I never told you my name.' She says'")
            time.sleep(4)
            print("'I'm Dr. Hazel Locklin, and I'm your Doctor.'")
            time.sleep(4)
            print("'What's your name?'")
            time.sleep(5)
            print("'...'")
            time.sleep(4)
            print("'Don't want to say? That's alright. We'll have plenty of time for you to get comfortable around me.' She says")
            time.sleep(5)
            print("For now, I want you to get some rest. I'm going to get somethings prepared and booked, and we'll talk in the morning, Okay?")
            time.sleep(5)
            print("'okay..' I mutter")
            time.sleep(3)
            print("The doctor walks out, They close the door and Lock it after turning off the lights")
            time.sleep(2)
            print("This doctor... They seem nice, Can I trust them?")
            print("Answer 1: I... Trust them")
            print("Answer 2: I... Don't Trust them")
            time.sleep(1)
            LocklinTrustinp = input("I... ")
            if "Trust them" in LocklinTrustinp:
                time.sleep(2)
                print("They seem trust worthy...")
                time.sleep(2)
                print("I think they just want to help..")
                time.sleep(2)
                print("That's a nice thought.")
                Melancholy.trauma1r(trauma)
                time.sleep(5)
                IVStamCheckFailMerge(trauma, health, stamina, progress, panicked)
            elif "Don't" in LocklinTrustinp:
                print("They seem untrustworthy...")
                time.sleep(2)
                print("I can't let my guard down, I need to be careful.")
                time.sleep(2)
                print("They seem too nice.")
                Melancholy.trauma1(trauma)
                time.sleep(3)
                IVStamCheckFailMerge(trauma, stamina, health, progress, panicked)

    if panicked == False:
        time.sleep(4)
        print("'hm?' The doctor says, They glance down at you")
        time.sleep(4)
        print("'Ah, your awake!' She says as she puts down her notepad")
        time.sleep(4)
        print("'Now, I need to ask you a few questions, and I need you to answer them honestly.'")
        time.sleep(4)
        print("'Do you know your last name?'")
        time.sleep(4)
        print("'...'")
        time.sleep(2)
        print("'Not one for conversation are you?' She says with a slight smile")
        time.sleep(4)
        print("'Well that's alright, I'll just have to ask you some more questions.'")
        time.sleep(4)
        print("'We can get to the other questions you didn't answer later.'")
        time.sleep(3)
        print("'Do you know where you are?'")
        act = input("I am are in a... ")
        if "Hospital" in act or "Clinic" in act or "infirmary" in act or "ER" in act or "Emergency Room" in act:
            time.sleep(2)
            print("You think back to when you woke up... you were in a Medical institution.")
            time.sleep(2)
            act = input("Do you answer honestly? (A: Yes) or (A: No) : ")
            if "Yes" in act or "Y" in act:
                print("You nod your head and smile")
                time.sleep(4)
                print("'Yes, you are in a Hospital!' She says as she writes down your answer")
                time.sleep(4)
            if "No" in act or "N" in act:
                print("You shake your head and look at them with a slight frown")
                time.sleep(4)
                print("'Oh, I see..' She says as she writes down your answer, returning a slight frown")
                time.sleep(4)
                print("'Well, your in a Hospital'")
                time.sleep(2)
        else:
            time.sleep(2)
            print("You think back to when you woke up... you didn't know where you were.")
            time.sleep(3)
            print("You shake your head and look at them with a slight frown")
            time.sleep(4)
            print("'Oh, I see..' She says as she writes down your answer, returning a slight frown")
            time.sleep(4)
            print("'Well, your in a Hospital'")
            time.sleep(2)
        print("'Now, Do you know what happened to you?'")
        time.sleep(3)
        print("'Or rather, what happened to make you need to come here?'")
        time.sleep(4)
        print("I try to think back, but I can't remember anything relevant.")
        time.sleep(4)
        print("I was walking down a lonely street with some friends, and then I woke up here.")
        time.sleep(4)
        print("I shake my head")
        time.sleep(3)
        print("'Well, that's alright. We can determine it with the help of modern technology.' She says")
        time.sleep(4)
        print("'Your Injuries were quite extensive.'")
        Melancholy.trauma1(trauma)
        time.sleep(2)
        print("'Now now, Don't worry about that. You're safe now. I wont let anyone hurt you.'")
        time.sleep(4)
        print("Their voice is soothing, You feel better.")
        time.sleep(1)
        Melancholy.trauma3r(trauma)
        print("")
        print("[!] Theraputic actions")
        print("Theraputic actions are actions that help you recover from trauma.")
        print("You can hire or randomly encounter these actions.")
        print("Lower trauma levels will help you have more control over your environment.")
        print("You can only check your trauma level by checking at the Therapists.")
        print("")
        a = input("Press enter to continue")
        print("")
        print("The door closes and the doctor says 'I'm back!'")
        time.sleep(3)
        print("You didn't even notice them leave?")
        time.sleep(3)
        print("You wave at them and smile")
        time.sleep(4)
        print("A Face of annoyance appears on their face 'Oh who did this to you?' They say")
        time.sleep(3)
        print("You look at them with a hint of fear as they get closer..")
        time.sleep(1)
        print("But why? They have only been kind..")
        time.sleep(5)
        print("They grab the IV Drip tangled around your sleeve and carefully take it off")
        Melancholy.trauma1r(trauma)
        time.sleep(3)
        print("They look at you with a smile and say 'There we go!~'")
        time.sleep(2)
        print("She gets close enough for you to be able to read their nametag")
        time.sleep(2)
        print("It says 'Dr. Hazel Locklin' on it")
        time.sleep(4)
        print("You smile at Hazel")
        time.sleep(2)
        print("'You're welcome!' She says as they put the IV Drip in a nearby trash can")
        time.sleep(3)
        print("'You won't be needing this anymore' She says")
        time.sleep(3)
        print("They sit down next to you and say 'So, what's your name?'")
        time.sleep(3)
        print("'Ah, I'm sorry I never told you my name.' She says'")
        time.sleep(4)
        print("'I'm Dr. Hazel Locklin, and I'm your Doctor.'")
        time.sleep(4)
        print("'What's your name?'")
        time.sleep(5)
        print("'...'")
        time.sleep(4)
        print("'Don't want to say? That's alright. We'll have plenty of time for you to get comfortable around me.' She says")
        time.sleep(5)
        print("For now, I want you to get some rest. I'm going to get somethings prepared and booked, and we'll talk in the morning, Okay?")
        time.sleep(5)
        print("'okay..' I mutter")
        time.sleep(3)
        print("Hazel smiles at me and walks out, She closes the door and Lock it after turning off the lights")
        time.sleep(2)
        print("This doctor... They seem nice, Can I trust them?")
        print("Answer 1: I... Trust them")
        print("Answer 2: I... Don't Trust them")
        time.sleep(1)
        LocklinTrustinp = input("I... ")
        if "Trust them" in LocklinTrustinp:
            time.sleep(2)
            print("They seem trust worthy...")
            time.sleep(2)
            print("I think they just want to help..")
            time.sleep(2)
            print("That's a nice thought.")
            Melancholy.trauma1r(trauma)
            time.sleep(5)
            IVStamCheckFailMerge(trauma, health, stamina, progress, panicked)
        elif "Don't" in LocklinTrustinp:
            print("They seem untrustworthy...")
            time.sleep(2)
            print("Why though? They've done nothing to deserve my mistrust")
            time.sleep(2)
            print("They seem so nice as well...")
            Melancholy.trauma1(trauma)
            time.sleep(3)
            IVStamCheckFailMerge(trauma, stamina, health, progress, panicked)

def IVStamCheckFailMerge(trauma, health, stamina, progress, panicked):
    print("")

# Calls the Def for Chapter1 if progress is 0
if progress == 0:
    Chapter1(trauma, stamina, progress, health)

# Calls the Def for Chapter1.1 if progress is 0.1
if progress == 0.1:
    Chapter1_1(trauma, stamina, progress, health)

Melancholy.endmsg(gamename=gamename, EOL=False)