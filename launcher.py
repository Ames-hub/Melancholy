from lib.essentials import *
from lib.printing import *
printing = printing()

log("Starting "+name_of_game)
log("Checking for save file...")

def clear_console(): os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

if save.exists() == True:
    erase = await_choice(printing.colours["cyan"]+"A save file was found. Would you like to "+printing.colours["yellow"]+"load it"+printing.colours["cyan"]+" or "+printing.colours["red"]+"erase it?"+printing.colours["cyan"]+" Press enter for Load", lower=False)
    if "e" in erase or "del" in erase: # Erase save file
        if save.erase() == True:
            printing.delay("Save file erased. Please restart the game", color="cyan")
            exit()
        else:
            printing.delay(
                "Save file could not be erased. Please remove the file 'lib/data/save.json' and restart the game",
                color="red"
                )
            exit()
    elif "l" in erase:
        printing.delay("Got it! Loading save file...", color="green")
        sleep(2)
        clear_console()
    else:
        clear_console()
else:

    # Creates a new save file if one doesn't exist
    while True: # Retry logic start
        name = await_choice(colours["cyan"]+"I name the child... "+colours["clear"], lower=False)
        name = name.capitalize()
        
        # Verifies this is the right name
        if "y" not in await_choice(name+"... is this the name you desire?", delay=0.1):
            printing.delay("Let us try again then..", color="cyan")
            sleep()
            clear_console()
            continue
        else:
            break

    save.save(
        player_name=name,
        player_location="old_home",
        player_inventory=save_file_dt["player"]["inventory"],
        chapter=0
    )
    log("Created new save file")
    printing.delay(
        name+"... May you never be the same again...", 
        0.3, print_faster=(name + " and may you never be the same again", 0.2))
    time.sleep(3)
    clear_console()

if get("player.progress") == 0: # Chapter 0
    from lib.chapters.Chapter0 import chapter
    chapter1_end = chapter.start()
else:
    printing.delay("No further chapters found.\nYou have reached the end.\nThank you for playing!", color="red")