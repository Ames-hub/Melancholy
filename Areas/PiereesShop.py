import sqlite3
import time
import logging

# Sets up logging
logging.basicConfig(filename='game.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info ("PiereesShop.py has been loaded")

con = sqlite3.connect('game.db')
cur = con.cursor()

# Imports the player money from the database
cur.execute("SELECT money FROM stats")
money = cur.fetchone()[0]
logging.info ("PiereesShop.py has imported the player's money from the database")

cur.execute("SELECT pieeresshop FROM FirstVisit")
visitedshop = cur.fetchone()[0]
logging.info ("PiereesShop.py has imported if the player has visited the shop from the database")

cur.execute("SELECT sanity FROM Stats")
sanity = cur.fetchone()[0]
logging.info ("PiereesShop.py has imported the player's sanity from the database")

cur.execute("SELECT * FROM dev")
debug = cur.fetchone()[0]
logging.info ("PiereesShop.py has imported if the player is in debug mode from the database")

#
# THE SHOP LIST AND ITS PRICES
#

# Clothing

Gray_Winter_Hoodie = "A Hoodie, Brand new and comfortable.", "Theraputic... Trauma raises slower while wearing"
Black_Skirt = "A Black Skirt, Perfect for any occasion."
White_Sneakers = "A pair of White Sneakers, Good for running. Reduces stamina drain"
Blue_Pajamas = "Blue Pajamas, Perfect for sleeping. Increases Stamina once used in sleep"
Black_Pants = "Black Pants, Perfect for any occasion."
Black_Track_Shorts = "Black Track Shorts, Perfect for running. Increases max stamina while wearing"
Gray_shirt = "A Gray Shirt, Plain and simple. A bit scratchy"

#
# THE SHOP LIST AND ITS PRICES
#

if debug == True:
    print(sanity, "Sanity")
    print(visitedshop, "Visited Shop")
    print(money, "Money")
    print(debug, "Debug")

# Runs if the player has not visited the shop before
if visitedshop == 0 and sanity > 60:
    time.sleep(1)
    print("Ah, welcome to my shop! I'm Pierre. I specialize in selling clothing and food.")
    time.sleep(3)
    print("However, I also sell basic neccesities for dangerous area's such as this place.")
    time.sleep(4)
    print("I'm sure you'll find something you like here. So, That being said. What can I do for you?")
    cur.execute("UPDATE FirstVisit SET pieeresshop = 1")
    time.sleep(2)
    if debug == True:
        print("Updated FirstVisit.pieeresshop to 1")

if visitedshop == 0 and sanity < 60:
    time.sleep(1)
    print("Ah, new customer! welcome to my shop! I'm... Pierre, I sell food and clothing..")
    time.sleep(4)
    print("...")
    time.sleep(3)
    print("?")
    time.sleep(2)
    print("I'm sorry, Are you alright?")
    time.sleep(1)
    print("You look a little.. off.")
    time.sleep(3)
    print("I don't mean to be rude, But I worry. Even for a stranger, If you want to talk, do let me know.")
    print("[!] New option Available! Talk to Pierre")
    therpiereest = 1
    # Inserts into the table "Special"
    cur.execute("INSERT INTO Special VALUES(?)", (therpiereest))
    if debug == True:
        print("Inserted thepiereest into Special")

con.commit()
if debug == True:
    print("Committed changes to the database")

import random

# GENERATES A RANDOM GREETING
def randgreet():
    g1 = "I apologize that I still dont have much to offer, But I'm sure you'll find something you like here."
    g2 = "You seem different today, New haircut? New clothes? It looks good on you whatever it may be!"
    g3 = "Pieere throws something out the window, and you hear a loud crash. 'Oh Hello I didn't expect to see anyone Today! Don't mind that, its nothing!... No, Dont go and check what it was.'"
    g4 = "'Pip, Stop that! You're making a mess!' Pieree looks at you and says 'Haha children, am I right? Good to see you today.'"
    g5 = "I heard some crazy man yell out about a person from another world constantly talking to us to raise something called a 'sanity stat' and how creators wouldn't want us to do that. What a crazy idiot."
    i = random.randint(1, 4)
    if i == 1:
        logging.info("Successfully returned a random greeting. g1 (Pieree's Shop)")
        return g1
    if i == 2:
        logging.info("Successfully returned a random greeting. g2 (Pieree's Shop)")
        return g2
    if i == 3:
        logging.info("Successfully returned a random greeting. g3 (Pieree's Shop)")
        return g3
    if i == 4:
        logging.info("Successfully returned a random greeting. g4 (Pieree's Shop)")
        return g4
    i = random.randint(0, 6969)
    if i == 6969:
        logging.info("Rare event triggered. (Pieree's Shop) 1 in 6969 chance.")
        return g5
    else:
        logging.error("FAILED TO RETURN A RANDOM GREETING. (Pieree's Shop)")
        return "Sorry, This is an error handling message. "
        

if visitedshop == 1 and sanity > 60:
    print("Welcome back!")
    time.sleep(1)
    print(randgreet())
    time.sleep(3)
    print("So, That being said. What can I do for you?")
    time.sleep(2)

print("You have ", money, " dollars.")
time.sleep(1)
print("What would you like to do?")
print("1. Leave") # Fuck, "Leave" is gonna be a can of worms.
print("2. Browse what the store offers")
print("3. Speak with pieree")

action = input("I... ")
logging.info("Player chose to " + action + " at pieeres shop.")

# Checks if the variable action contains the string "Browse"
if "Browse" or "2" or "Buy" in action:
    print("What do you want to view?")
    print("1. Food")
    print("2. Clothing")
    print("3. Back")
    action = input
    if "Clothing" or "2" in action:
        print("You look around, Not much catches your attention.")
        time.sleep(2)
        print("You see a few things that you might be interested in.")
        time.sleep(2)
        print("")
        print("1", Gray_Winter_Hoodie)
        time.sleep(1)
        print("")
        print("2", Black_Skirt)
        time.sleep(1)
        print("")
        print("3", White_Sneakers)
        time.sleep(1)
        print("")
        print("4", Blue_Pajamas)
        time.sleep(1)
        print("")
        print("5", Black_Pants)
        time.sleep(1)
        print("")
        print("6", Black_Track_Shorts)
        time.sleep(1)
        print("")
        print("7", Gray_shirt)