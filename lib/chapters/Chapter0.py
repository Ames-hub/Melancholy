from ..printing import printing as pr
from ..save import get
from ..essentials import sleep, await_choice, log
pr = pr(default_colour="cyan")

class chapter: # Can always "import as" for renaming
    def start():
        '''
        Start chapter 0: Pilot
        '''
        log("Starting Chapter 0: Pilot")
        chapter.p1()

    def p1(): 
        pr.solid_color("The world stirs awake.. Your eye's flutter as you wake up")
        sleep()
        pr.solid_color("You look around your room, messy, littered with toys..\nA Surreal and cheerful fealing washes over you!")
        sleep(5)
        pr.solid_color("You jump out of bed! Giggling as the new day starts to unfold!")
        sleep()
        text = (
            "You run to the door, and open it!\n"
            f"{pr.colors['green']} ! Notice ! Option hints are shown here\n\n"
            "(1: door) It reveals a long hallway with a door to the side, that's my mums room!\n"
            "(2: stairs) It also reveals a staircase at the end... They don't want me going down there..."
        )
        
        global looped_once
        looped_once = False # This becomes True if the player has gone to the stairs or the door and not both
        global dining_room_available
        dining_room_available = False
        gone_to_doorway = False
        gone_to_stairs = False
        while not (gone_to_stairs and gone_to_doorway): # Starts a "Choose both ways" loop
            if gone_to_stairs == True and gone_to_doorway == True:
                break
            
            def stairs(done=False):
                if done == False:
                    pr.delay("I walk cautiously to the stairs.. This.. feels bad..", print_faster=("This...", 0.1), delay=0.15)
                    sleep(1)
                    pr.delay(
                        "The stairs get closer and closer and I feel more and more weird... I.. should stop now..",
                        print_faster=("I.. should stop now..", 0.1),
                        delay=0.23
                        )
                    sleep(3)
                    pr.partial_solid(
                        "\nI stop.. wait for a moment and turn around, Its not right.. they trust me to not go down there.. I wont!",
                        target="I wont!",
                        target_color="red",
                        default_color="green"
                        )
                    await_choice(pr.colors["red"]+"I walk back to the door way...")
                else:
                    pr.partial_solid(
                        text="I've already been to the stairs.. I wont go back there.",
                        target="I don't want to go back there..",
                        target_color="red",
                        default_color="green"
                    )

            if dining_room_available == True:
                pr.color_text(
                    "(1: door) It reveals a long hallway with a door to the side, that's my mums room!\n"
                    "(2: stairs) It also reveals a staircase at the end... They don't want me going down there..."
                    "(3: dinning room) I should go to the dinning room! But only if thats the last thing I wanna do here!",
                    color="green"
                )
            else:
                pr.color_text(
                    "(1: door) It reveals a long hallway with a door to the side, that's my mums room!\n"
                    "(2: stairs) It also reveals a staircase at the end... They don't want me going down there...",
                    color="green"
                )

            if gone_to_stairs == True:
                text = (
                    "(1: door) It reveals a long hallway with a door to the side, that's my mum's room!\n"
                    "(2: stairs) It also reveals a staircase at the end... I refuse to go there!"
                )
                if dining_room_available == True:
                    text = (
                        text+"\n(3: dinning room) I should go to the dinning room! But only if thats the last thing I wanna do here."
                    )
            elif gone_to_doorway == True:
                text = (
                    "(1: door) It reveals a long hallway with a door to the side, that's my mum's room! They seem happy at the moment :)\n"
                    "(2: stairs) It also reveals a staircase at the end... They don't want me going down there..."
                )
                if dining_room_available == True:
                    text = (
                        text+"\n(3: dinning room) I should go to the dinning room! But only if thats the last thing I wanna do here."
                    )
            pr.solid_color(text)
            choice = await_choice(pr.colors["cyan"]+"Where do you go?", delay=0.05)
            
            # Handles Stair choice
            if gone_to_stairs == False:
                if choice == "stairs" or choice == "2":
                    stairs()
                    gone_to_stairs = True
                    looped_once = True
                    continue
            elif gone_to_stairs == True:
                if choice == "stairs" or choice == "2":
                    stairs(True)
                    continue
            
            def doorway(done=False):
                if done == False:
                    pr.delay("I approach the door to the hallway with anticipation!", delay=0.05, color="cyan")
                    sleep(3)
                    pr.solid_color(
                        "The hallway stretches before me, and my mum's bedroom door stands tall...",
                        color="cyan"
                    )
                    sleep(3)
                    pr.delay(pr.colors["cyan"]+"Taking a step forward, I open the door to my mum's room.", delay=0.09)
                    sleep(3)
                    pr.partial_solid(
                        "\nThe room is filled with their comforting presence!\nMy mum sit on the bed of her cozy room, facing away from me\nMy mum giggles to herself.. I wonder why?\n",
                        target="my mum giggle to herself.. I wonder why?",
                        target_color="green",
                        default_color="cyan"
                    )
                    sleep(7)
                    pr.partial_solid(
                        "Suddenly, she turns towards me with surprised expressions on her face! \""+get("player.name")+"\" She says, \"How are you doing!\" She says cheerfully",
                        target="surprised expressions on their faces!",
                        target_color="yellow",
                        default_color="cyan"
                    )
                    sleep(3)
                    pr.solid_color(
                        text="Before I can say anything, she pulls me close and hugs me..",
                        color="yellow"
                    )
                    sleep(5)
                    pr.partial_solid(
                        "Her love, Her warmth... Sometimes I forget how much She care about me...",
                        target="love",
                        target_color="red",
                        default_color="cyan"
                    )
                    sleep(5)
                    pr.partial_solid(
                        "She lets me go, and says softly \"I'll be out in a second "+get("player.name")+", wait for me in the dinning room, will you?\"",
                        target="wait for me in the dinning room, will you?",
                        target_color="yellow",
                        default_color="cyan"
                    )
                    sleep()
                    pr.color_text(
                        "I nod my head and run out of the room, closing the door behind me.",
                    )
                else:
                    pr.partial_solid(
                        text="They'll be out in a moment~ I wont bother them! ... For a minute!\nIn the meanwhile, I should go to the dinning room\n"+
                        pr.colors["green"]+"\nNew option available! (3: dinning room)",
                        target="... For a minute!",
                        target_color="red",
                        default_color="cyan"
                    )
                    global dining_room_available
                    dining_room_available = True

            # Handles Doorway choice
            if gone_to_doorway == False:
                if "door" in choice or "doorway" in choice or choice == "1":
                    doorway()
                    pr.partial_solid(
                        text="They'll be out in a moment~ I wont bother them! ... For a minute!\nIn the meanwhile, I should go to the dinning room\n"+
                        pr.colors["green"]+"\nNew option available! (3: dinning room)",
                        target="... For a minute!",
                        target_color="red",
                        default_color="cyan"
                    )
                    gone_to_doorway = True
                    looped_once = True
                    continue
            elif gone_to_doorway == True:
                if choice == "door" or choice == "1":
                    doorway(True)
                    continue