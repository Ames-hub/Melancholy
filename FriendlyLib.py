###################################################################
#                        FRIENDLY LIBRARY                         #
#                             PYTHON                              #
#                                                                 #
#       This is my private def library. It contains all the       #
#         functions that are commonly used in my programs.        #
#         (Yes, some of them specific to certain programs)        #
#                                                                 #
#                         Copyright © 2023                        #
#                           CC BY-NC 4.0                          #
###################################################################

import logging, time, colorama, sys, os, sqlite3, random

# Gets the name of the folder FriendlyLib.py is stored in
parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gamename = parent_path
con = sqlite3.connect(gamename + ".db")
cur = con.cursor()

# GENERIC FUNCTIONS
# GENERIC FUNCTIONS
# GENERIC FUNCTIONS

# Clears the console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def setting(system_name, experimental, description, con, cur):
    clear()
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
    clear()
    
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

# generates Weather
def gen_forecast_weather(cur):
        # Determines if the experimental_weather system is enabled
    # Determines if the weather system is enabled
    cur.execute("SELECT weather FROM settings")
    experimental_weather = cur.fetchone()[0]
    
    if experimental_weather == True:
        temperature = gen_forecast_temp()
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
    else:
        return "DISABLED"

# Generates Temp
def gen_forecast_temp(cur):
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

