# CHAPTER 1.0
# This is the first chapter of the game, it is the tutorial chapter
# Chapter 1.0 Is the story of the character's either peaceful exit or escape from the hospital
# Both routes teach the same components, but the easier route is the peaceful route.

import logging, time, sqlite3, sys, colorama, os

# THE END MESSAGE INDICATING WHEN THERE IS NO MORE STORY TO BE TOLD
def endmsg():
    time.sleep(10)
    clear()
    print("Sorry! But thats the end of Melancholy. I will continue to develop it :)")
    print_cword("Head over to my Github page if you want to check for updates!", "Github page", "green")
    print_color("https://github.com/Ames-Hub", "green")
    print("")
    print("Press CTRL + C to exit")

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

# Clears the console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

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

# Sets up logging
logging.basicConfig(filename='logs/Chapter1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sets up logging to put all errors in logs/Errors.log
logging.basicConfig(filename='logs/error.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()

con = sqlite3.connect('game.db')
cur = con.cursor()
logging.info("Connected to database")

logging.info ("Chapter1.py has been loaded")

ksfjis = True
if ksfjis == True:
    # Imports trauma from the DB
    cur.execute("SELECT trauma FROM stats")
    trauma = cur.fetchone()[0]
    logging.info("Trauma imported from DB")
    # Imports trauma from the DB
    # Imports Stamina from the DB
    cur.execute("SELECT stamina FROM stats")
    stamina = cur.fetchone()[0]
    logging.info("Stamina imported from DB")
    # Imports Stamina from the DB
    # Imports Health from the DB
    cur.execute("SELECT health FROM stats")
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
# Used to shrink all this shit

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
    clear()
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
            trauma1(trauma)
            time.sleep(3)
            print("I try to get out of the bed, but I am immediately pulled back.\nYou immediately notice the IV Drip, Its tangled up around the Bed frame and restraining you.")
            time.sleep(5)
            print("I try to pull it off, but it's too tight. I can't get it off! ")
            trauma1(trauma)
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
                print_cword("I struggle against the IV Drip cable, it doesn't budge", "it doesn't budge", "red") 
                time.sleep(2)
                print("'Hold them down! They're trying to escape!'\nThey say as they push me down and")
                s = "And..."
                delay_print(s)
                print("...")
                s = 'inject.. Something...'
                delay_print(s)
                IVStamCheckFail(health, stamina, trauma, progress)
        elif 'ok' in act or 'Ok' in act or 'Okay' in act or 'Okay' in act or "Fine" in act or "fine" in act:
            print("Whatever, its fine... its not what matters right now")
            time.sleep(2)
            print("I need to stay Calm, I'm sure everything will be explained soon enough.")
            time.sleep(3)
            print("I try to get out of the bed and stand up, But I'm pulled back by the IV drip. Its a bit tangled up")
            time.sleep(3)
            print_cword("I try to untangle it, but its not possible from where I am.", "not possible from where I am.", "red")
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
        print_cword("That... somehow doesn't sound right", "somehow doesn't sound right", "red")
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
        trauma2(trauma)
        time.sleep(2)
        print("Wait... I can't remember anything, Where's my memory!? What's happening!")
        trauma1(trauma)
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
            trauma1(trauma)
            time.sleep(2)
            print("A group of people in clean white suits rushes in, Why are they here!?")
            time.sleep(2)
            print("'Hold them down! They're trying to escape!'\nThey say as they push me down and")
            s = "and..."
            delay_print(s)
            print("...")
            s = 'inject.. Something...'
            trauma1(trauma)
            delay_print(s)
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
    delay_print('"Attention all staff, a code amber has been declared for 112."')
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
            trauma1(trauma)
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
            delay_print("'Woah champ, slow down! You're going to hurt yourself!'")
            time.sleep(3)
            if trauma > 300:
                # Prints in red "You look at the man, stunned with fear"
                print_color("You look at the man, stunned with fear", "red")
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
                trauma3r(trauma)
                print_cword("Their voice is oddly calming", "calming", "blue")
                time.sleep(3)
                print_cword("You must be why they called a amber alert", "amber alert", "yellow")
                time.sleep(3)
                print("Do not worry, I do not know why you chose to ran. but I will not let them harm you.")
                time.sleep(5)
                trauma2r(trauma)
                # Create's a new table called "TallStrongProt"
                cur.execute('''CREATE TABLE IF NOT EXISTS TallStrongProt (TSP integer PRIMARYKEY)''')
                TSP = 1
                cur.execute("INSERT INTO TallStrongProt VALUES (?)", (int(TSP),))
                con.commit
                savestat(stamina, trauma, health)
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
                print_cword("'Ah. So your why they declared a code amber", "code amber", "yellow")
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
                        savestat(stamina, trauma, health)
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
                        print_cword("You feel a sudden wave of Exhaustion...", "Exhaustion", "blue")
                        delay_print("You fall asleep...")
                        savestat(stamina, trauma, health)
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
                    print_cword("You feel a sudden wave of Exhaustion...", "Exhaustion", "blue")
                    delay_print("You fall asleep...")
                    savestat(stamina, trauma, health)
                    IVStamCheckFail(trauma, health, stamina, progress, panicked=True)
        # THIS IS CORRECTLY INDENDTED DONT FUCKING CHANGE IT
        # This is the path where the player encounter's guards when turning right
        elif "right" in act or "Right" in act:
            print("I run to the right hallway.")
            time.sleep(5)
            print("I turn the corner and see 4 guards walking my way, They haven't seen me yet! What do I do?!")
            trauma1(trauma)
            time.sleep(3)
            print("")
            print("[!] Detective work is possible here, but not required")
            print("")
            time.sleep(3)
            print("Ok calm down, Think...")
            time.sleep(2)
            print("There's a cleaning closet to my right, I could hide in there!")
            print_cword("Option: Hide", "Hide", "blue")
            time.sleep(4)
            print("Or I could run down the hallway past the guards and try to escape!")
            print_cword("Option: Run", "Run", "Red")
            time.sleep(3)
            act = input("I... ")
            if "Hide" in act or "hide" in act:
                print("I run to the closet and I open the door and close it behind me")
                time.sleep(2)
                print("I slowly close it to keep quiet and I wait for the security to pass")
                time.sleep(2)
                print("I hear footsteps getting closer and closer")
                trauma1(trauma)
            elif "Run" in act or "run" in act:
                print("I run down the hallway as fast as I can!")
                time.sleep(2.5)
                print("The security guards look at me running past them, A couple try to grab me but I barely move out of the way")
                trauma1(trauma)
                time.sleep(2.5)
                print("2 of the guard's yell 'HALT!' and start running towards me while the other 2 run around the corner")
                time.sleep(2.5)
                print("They yell, 'Damnit, Slow down! We aren't gonna hurt you!'")
                time.sleep(2.5)
                print("One of the guard's stumble, They fall down and hit their head, Dazing them")
                time.sleep(2.5)
                print("The other one however, They are gaining on me!")
                trauma1(trauma)
                time.sleep(2.5)
                print_cword("I run as fast as I can, but they catch me", "but they catch me", "red")
                time.sleep(2.5)
                print("They grab me from behind and pull me up by my arms until my feet don't touch the floor")
                time.sleep(3.5)
                print("[!] Stamina check")
                if stamina > 440:
                    print("with all my strength, I raise my legs up to their face and kick them")
                    print_color("Stamina -", "red")
                    stamina =- 20
                    savestat(stamina, trauma, health)
                    print("They stumble and I run towards the exit, I open the door and dash out")
                    time.sleep(5)
                    print("I kept running for what felt like days")
                    time.sleep(3)
                    delay_print("I eventually... passed... out...")
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
                    delay_print("You fall asleep...")
                    logging.info("User sent to IVStamCheckFail")
                    IVStamCheckFail(stamina, health, trauma, progress)

def Chapter1_1(trauma, stamina, health, progress):
    print("wow")
    savestat(stamina, trauma, health)
    endmsg()


# The end for if the user did not have the stamina to escape the Tangled up IV cord
def IVStamCheckFail(trauma, health, stamina, progress, panicked):

    # Inserts into the DB that Hazel was met.
    cur.execute("INSERT INTO MetHazel VALUES (?)", (int(1),))

    if panicked == True:
        time.sleep(4)
        clear()
        savestat(stamina, trauma, health, con, cur)
        delay_print("You wake up... You feel tired and dazed")
        time.sleep(3)
        print("...")
        delay_print("A Doctor stands next to you.. Is that who that was?")
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
            delay_print("I shake my head")
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
            trauma1(trauma)
            time.sleep(2)
            print("'Now now, Don't worry about that. You're safe now. I wont let anyone hurt you.'")
            time.sleep(4)
            print("Their voice is soothing, You feel better.")
            time.sleep(1)
            trauma3r(trauma)
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
            trauma1r(trauma)
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
                trauma1r(trauma)
                time.sleep(5)
                IVStamCheckFailMerge(trauma, health, stamina, progress, panicked)
            elif "Don't" in LocklinTrustinp:
                print("They seem untrustworthy...")
                time.sleep(2)
                print("I can't let my guard down, I need to be careful.")
                time.sleep(2)
                print("They seem too nice.")
                trauma1(trauma)
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
        trauma1(trauma)
        time.sleep(2)
        print("'Now now, Don't worry about that. You're safe now. I wont let anyone hurt you.'")
        time.sleep(4)
        print("Their voice is soothing, You feel better.")
        time.sleep(1)
        trauma3r(trauma)
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
        trauma1r(trauma)
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
            trauma1r(trauma)
            time.sleep(5)
            IVStamCheckFailMerge(trauma, health, stamina, progress, panicked)
        elif "Don't" in LocklinTrustinp:
            print("They seem untrustworthy...")
            time.sleep(2)
            print("Why though? They've done nothing to deserve my mistrust")
            time.sleep(2)
            print("They seem so nice as well...")
            trauma1(trauma)
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

endmsg()