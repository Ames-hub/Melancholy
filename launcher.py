from lib.essentials import *
from lib.printing import *
printing = printing()

log("Starting "+name_of_game)
log("Checking for save file...")

def clear_console(): os.system('cls' if os.name == 'nt' else 'clear')

clear_console()
if save.exists() == False:
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
        name+"... Take this advice from me..\nTreat this as an adventure, and may you never be the same again...", 
        0.3, print_faster=(name + " and may you never be the same again", 0.2))
    time.sleep(3)
    clear_console()

from lib.chapters.Chapter0 import chapter
chapter1_end = chapter.start()