import time, sqlite3, logging, random, os, sys, colorama

# Imports trauma and health and stamina from the DB

# The DB
con = sqlite3.connect('game.db')
cur = con.cursor()

logging.info("Importing stats from DB")
cur.execute("SELECT trauma FROM stats")
trauma = cur.fetchone()[0]

# Imports stamina
cur.execute("SELECT stamina FROM stats")
stamina = cur.fetchone()[0]
cur.execute("SELECT maxstamina FROM stats")
maxstamina = cur.fetchone()[0]
cur.execute("SELECT minstamina FROM stats")
minstamina = cur.fetchone()[0]

# imports health
cur.execute("SELECT health FROM stats")
health = cur.fetchone()[0]
cur.execute("SELECT maxhealth FROM stats")
maxhealth = cur.fetchone()[0]
cur.execute("SELECT mingenhealth FROM stats")
mingenhealth = cur.fetchone()[0]

# Clears the console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# THE END MESSAGE INDICATING WHEN THERE IS NO MORE STORY TO BE TOLD
def endmsg(gamename):
    time.sleep(10)
    clear()
    print("Sorry! But thats the end of " + gamename + ". I will continue to develop it :)")
    print("Head over to my Github page if you want to check for updates!")
    print("https://github.com/Ames-Hub")
    print("")
    print("Press CTRL + C to exit")

def endmsgEOL(gamename):
    time.sleep(10)
    clear()
    print("Sorry! But thats the end of " + gamename)
    print("Unfortunately, This game has reached its EOL and will no longer be updated.")
    print("If you liked" + gamename + ", over to my Github page if you want to check for more content made by me!")
    print("https://github.com/Ames-Hub")
    print("")
    print("Press CTRL + C to exit...")
    time.sleep(5000)
    print("")
    delay_print("You're still here? Well, I guess you can stay a little longer if you Really want to hang on")

# Prints a str 1 letter at a time
def delay_print(s):
    logging.info("Function 'delay_print' has been called")
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

# Prints a str in a certain color
def print_color(text, color):
    logging.info("Function 'print_color' has been called")
    colorama.init()
    colors = {
        "red": colorama.Fore.RED,
        "green": colorama.Fore.GREEN,
        "yellow": colorama.Fore.YELLOW,
        "blue": colorama.Fore.BLUE,
        "magenta": colorama.Fore.MAGENTA,
        "cyan": colorama.Fore.CYAN,
        "white": colorama.Fore.WHITE,
    }
    print(colors[color] + text)
    colorama.deinit()

# Prints a str and 1 word in that string as a certain color
def print_cword(text, word, color):
    logging.info("Function 'print_cword' has been called")
    colorama.init()
    colors = {
        "red": colorama.Fore.RED,
        "green": colorama.Fore.GREEN,
        "yellow": colorama.Fore.YELLOW,
        "blue": colorama.Fore.BLUE,
        "magenta": colorama.Fore.MAGENTA,
        "cyan": colorama.Fore.CYAN,
        "white": colorama.Fore.WHITE,
    }
    print(text.replace(word, colors[color] + word + colorama.Style.RESET_ALL))
    colorama.deinit()

# SAVES ALL STATS
def savestat(trauma, stamina, health, con, cur):
    cur.execute("UPDATE stats SET trauma = ?", (trauma,))
    logging.info("Saved Trauma to DB")
    cur.execute("UPDATE stats SET stamina = ?", (stamina,))
    logging.info("Saved Stamina to DB")
    cur.execute("UPDATE stats SET health = ?", (health,))
    logging.info("Saved Health to DB")
    con.commit()

# ADDS TRAUMA
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

# REMOVES TRAUMA
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

# Logging
logging.basicConfig(filename='logs/FreeRoam.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def forecast_temp():
    '''This function determines the in-game weather'''
    logging.info('forecast def called')

    # Determines if the weather system is enabled
    experimental_temperature = True

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
            act = random.randint(1, 50)
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

            # Learn how to make the weather persistent for a few days at a time

def forecast_weather():
        # Determines if the experimental_weather system is enabled
    experimental_weather = True
    
    if experimental_weather == True:
        temperature = forecast_temp()
        if temperature < 0:
            weather = "snow"
        elif temperature < 10:
            weather = "cloudy"
            act = random.randint(1, 15)
            if act > 5 or act < 8:
                weather = "rain"
        elif temperature > 30:
            weather = "clear"
        elif temperature > 35:
            weather = "sunny"

        return weather


# Prints a random opening depending on env var's everytime its called
def RandomOpening(trauma):
    logging.info('RandomOpening def called')
    act = random.randint(1, 3)
    # WEATHER RESPONSES
    # COLD WEATHER
    if act == 1:
        temperature = forecast_temp()
        weather = forecast_weather()
        if temperature < 18:
            print("I walk around the city, a cool breeze flows by. Brr!")
            if weather == "snow":
                logging.warning("Weather: SNOW is true and temperature is above 0c")
            if weather == "cloudy":
                print("The sky is cloudy, I hope it doesn't rain...")
            if weather == "rain":
                abc = random.randint(1, 2)
                if abc == 3:
                    print("Its raining, Just my luck...")
                if abc == 2:
                    print("Its raining, I should probably get an umbrella...")
                if abc == 1:
                    print("Its raining, Guess I'll stay under shelter as I go")
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
                delay_print("Its a beautiful day outside... Birds are singing... Flowers are blooming... On days like these, kids like you... S h o u l d   b e   b u r n i n g   i n   h e l l .")
                if weather == "cloudy":
                    print("Sure are a lot of clouds, fingers crossed for no rain!")
                elif weather == "rain":
                    delay_print("P e r f e c t . Rain, on such a nice day")
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
                trauma3(trauma)
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
    
def FreeRoam(trauma):
    logging.info('FreeRoam.py started')
    RandomOpening(trauma)

# NOT CURRENTLY FUNCTIONAL