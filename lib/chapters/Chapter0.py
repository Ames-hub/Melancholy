from ..printing import printing as pr
from ..save import get
from ..essentials import sleep, await_choice, log, locget, save_data, add_data, clear_console
pr = pr(default_colour="cyan")

class chapter: # Can always "import as" for renaming
    def start():
        '''
        Start chapter 0: Pilot
        '''
        log("Starting Chapter 0: Pilot")
        progress = get("player.progress")
        # Part 0
        if progress == 0:
            p0_ending = chapter.p0()
            save_data(key="endings.c0.p0.went_to_basement", value=p0_ending)
            save_data("player.progress", 0.1)
            progress = 0.1
        else:
            p0_ending = False

        # Part 1
        if progress == 0.1:
            p1_ending = chapter.p1()
            save_data(key="endings.c0.p2.object_choice", value=p1_ending)
            save_data("player.progress", 0.2)
            progress = 0.2
        else:
            p1_ending = False

        # Part 2
        if progress == 0.2:
            p2_ending = chapter.p2()
            # No data to save other than progress
            save_data("player.progress", 0.3)
            progress = 0.3

    def p0(): 
        pr.solid_colour("The world stirs awake.. Your eye's flutter as you wake up")
        sleep()
        pr.solid_colour("You look around your room, messy, littered with toys..\nA Surreal and cheerful feeling washes over you!")
        sleep(5)
        pr.solid_colour("You jump out of bed! Giggling as the new day starts to unfold!")
        sleep()
        pr.solid_colour(
            text="You run to the door, and open it!",
            colour="cyan"
        )    
        try:
            input(pr.colours["green"]+"Press enter to continue...\n")
        except: # Don't allow an exception to stop the game
            pass

        text = (
            f"{pr.colours['green']} ! Notice ! Option hints are shown here\n\n"
            "(1: door) The newly open door reveals a long hallway with a door to the side, that's my mums room!\n"
            "(2: stairs) It also reveals a stair spiral at the end... They don't want me going down there..."
        )
        
        global looped_once
        looped_once = False # This becomes True if the player has gone to the stairs or the door and not both
        global dinning_room_available
        dinning_room_available = False
        dinning_room_activated = False
        gone_to_doorway = False
        global gone_to_stairs
        gone_to_stairs = False
        while not (gone_to_stairs and gone_to_doorway and dinning_room_activated): # Starts a "Choose both ways" loop
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
                    sleep(6)
                    pr.solid_colour(
                        "\nI go down the staircase... My heart pounding..",
                        colour="cyan"
                        )
                    sleep(6)
                    pr.solid_colour(
                        "And suddenly.. I hear a voice.. Its my mum's? but.. she's in her room?",
                        colour="cyan"
                        )
                    sleep(5)
                    pr.solid_colour(
                        "I peer around the corner...",
                        colour="cyan",
                        )
                    sleep(3)
                    pr.delay(
                        text="I see my mum, standing in the newly found room of the basement, with her back towards me..",
                        delay=0.05, colour="cyan"
                        )
                    sleep(5)
                    pr.delay(
                        text="She's holding pills.. and a bottle of water.. What are they for?",
                        delay=0.1, colour="cyan"
                        )
                    sleep(5)
                    pr.delay(
                        text="She swallows 3 pills, and puts the bottle down..",
                        delay=0.05, colour="cyan"
                        )
                    sleep(5)
                    pr.delay(
                        text="She says after she does so.. \"Ahg...\" she breathes heavily..\n\"Do it for "+get("player.name")+".. You can keep going.. until they're strong enough..\"",
                        delay=0.2, colour="cyan"
                        )
                    sleep(5)
                    pr.delay(
                        text="The pills. they look like.. Antidepressants?",
                        delay=0.05, colour="cyan"
                        )

                    await_choice(pr.colours["red"]+"This is wrong.. I leave, walking back to the hallway...")
                else:
                    pr.partial_solid(
                        text="I've already been to the stairs.. I wont go back there.",
                        targets=["I don't want to go back there.."],
                        target_colours=["red"],
                        default_colour="green"
                    )

            if dinning_room_available == True:
                pr.colour_text(
                    "(1: door) It reveals a long hallway with a door to the side, that's my mums room!\n"
                    "(2: stairs) It also reveals a spiral of stairs at the end... They don't want me going down there..."
                    "(3: dinning room) I should go to the dinning room! But only if thats the last thing I wanna do here!",
                    colour="green"
                )
            else:
                pr.colour_text(
                    "(1: door) It reveals a long hallway with a door to the side, that's my mums room!\n"
                    "(2: stairs) It also reveals a spiral of stairs at the end... They don't want me going down there...",
                    colour="green"
                )

            if gone_to_stairs == True:
                text = (
                    "(1: door) It reveals a long hallway with a door to the side, that's my mum's room!\n"
                    "(2: stairs) It also reveals a spiral of stairs at the end... I refuse to go there!"
                )
                if dinning_room_available == True:
                    text = (
                        text+"\n(3: dinning room) I should go to the dinning room! But only if thats the last thing I wanna do here."
                    )
            elif gone_to_doorway == True:
                text = (
                    "(1: door) It reveals a long hallway with a door to the side, that's my mum's room! They seem happy at the moment :)\n"
                    "(2: stairs) It also reveals a spiral of stairs at the end... They don't want me going down there..."
                )
                if dinning_room_available == True:
                    text = (
                        text+"\n(3: dinning room) I should go to the dinning room! But only if thats the last thing I wanna do here."
                    )
            pr.solid_colour(
                f'You are in {locget("old_home.name")}\n{locget("old_home.description")}\n'+text)
            choice = await_choice(pr.colours["cyan"]+"Where do you go?", delay=0.05)
            
            # Handles Stair choice
            if gone_to_stairs == False:
                if "stairs" in choice or choice == "2":
                    stairs()
                    gone_to_stairs = True
                    looped_once = True
                    continue
            elif gone_to_stairs == True:
                if "stairs" in choice or choice == "2":
                    stairs(True)
                    continue
            
            def doorway(done=False):
                if done == False:
                    pr.delay("I approach the door to the hallway with anticipation!", delay=0.05, colour="cyan")
                    sleep(3)
                    pr.solid_colour(
                        "The hallway stretches before me, and my mum's bedroom door stands tall...",
                        colour="cyan"
                    )
                    sleep(3)
                    pr.delay(pr.colours["cyan"]+"Taking a step forward, I open the door to my mum's room.", delay=0.09)
                    sleep(3)
                    pr.partial_solid(
                        "\nThe room is filled with their comforting presence!\nMy mum sit on the bed of her cozy room, facing away from me\nMy mum giggles to herself.. I wonder why?\n",
                        targets=["my mum giggle to herself.. I wonder why?"],
                        target_colours=["green"],
                        default_colour="cyan"
                    )
                    sleep(7)
                    pr.partial_solid(
                        "Suddenly, she turns towards me with surprised expressions on her face! \""+get("player.name")+"\" She says, \"How are you doing!\" She says cheerfully",
                        targets=["surprised expressions on her face!"],
                        target_colours=["yellow"],
                        default_colour="cyan"
                    )
                    sleep(3)
                    pr.solid_colour(
                        text="Before I can say anything, she pulls me close and hugs me..",
                        colour="yellow"
                    )
                    sleep(5)
                    pr.solid_colour(
                        "Her love, Her warmth... Sometimes I forget how much She care about me...",
                        colour="cyan"
                    )
                    if gone_to_stairs == True:
                        sleep()
                        pr.partial_solid(
                            text=".. As the memory of almost breaking your mums trust by going down the stairs comes back to you.. you feel a little guilty..",
                            targets=["you feel a little guilty.."],
                            target_colours=["red"],
                            default_colour="cyan"
                        )
                        sleep()
                        pr.delay(
                            text="My mum asks me \"What's wrong?\" I say...",
                            colour="cyan", delay=0.1
                        )
                        pr.delay(
                            text="\"Nothing! Nothing at all! I'm just happy to see you!\"",
                            colour="yellow", delay=0.1, print_faster=("Nothing! Nothing at all!", 0.02)
                        )
                        sleep()
                        pr.delay(
                            text="I think she frowns for a second.. but she smiles again and says \"I'm happy to see you too!\"",
                            colour="cyan"
                        )
                    sleep(5)
                    pr.partial_solid(
                        "She lets me go, and says softly \"I'll be out in a second "+get("player.name")+", wait for me in the dinning room, will you?\nI have a surprise for you!\"",
                        targets=["wait for me in the dinning room, will you?", "surprise"],
                        target_colours=["yellow", "yellow"],
                        default_colour="cyan"
                    )
                    sleep()
                    pr.colour_text(
                        "I nod my head and run out of the room, closing the door behind me.",
                        colour="cyan"
                    )
                else:
                    pr.partial_solid(
                        text="She'll be out in a moment~ I wont bother her! ... For a minute!\nIn the meanwhile, I should go to the dinning room\n"+
                        pr.colours["green"]+"\nNew option available! (3: dinning room)",
                        targets=["... For a minute!"],
                        target_colours=["red"],
                        default_colour="cyan"
                    )
                    global dinning_room_available
                    dinning_room_available = True

            # Handles Doorway choice
            if gone_to_doorway == False:
                if "door" in choice or choice == "1":
                    doorway()
                    pr.partial_solid(
                        text="She'll be out in a moment~ I wont bother them! ... For a minute!\nIn the meanwhile, I should go to the dinning room\n"+
                        pr.colours["green"]+"\nNew option available! (3: dinning room)",
                        targets=["... For a minute!"],
                        target_colours=["red"],
                        default_colour="cyan"
                    )
                    gone_to_doorway = True
                    looped_once = True
                    continue
            elif gone_to_doorway == True:
                if "door" in choice or choice == "1":
                    doorway(True)
                    continue

            if dinning_room_available == True:
                if "dinning" in choice or "dining" in choice or choice == "3":
                    dinning_room_activated = True

        return gone_to_stairs
                    
    def p1():
        # This loop only stops when both the stairs and the door have been visited AND the dinning room has been "gone to"
        # Therefore, we handle the dinning room choice here

        pr.delay(
        text="I walk to the dinning room, and sit down at the table, and wait for mum to come out of her room.",
        delay=0.05,
        colour="cyan",
        )
        sleep(8)
        pr.delay(
            text="...",
            delay=3,
            colour="cyan"
        )
        sleep(5)
        pr.delay(
            text="You put your head on the table",
            delay=0.05,
            colour="cyan"
        )
        sleep(5)
        pr.delay(
            text="You say to yourself, boredly,\nThis is taking too longgg~ what can I do to pass the time..",
            delay=0.1,
            colour="cyan"
        )
        sleep()
        pr.partial_solid(
            text=(
            "You look around the room, and you see..\n"
            "A Computer, not very powerful.. but it runs Melancholy\n"
            "A Bookshelf, filled with books, some of which mum has read to me.\n"
            "A Window, with a view of the outside world, and the sun shining through. Its a warm and sunny day!\n"),
            targets=["A Computer", "A Bookshelf", "A Window"],
            target_colours=["green", "green", "green"],
            default_colour="cyan"
        )
        sleep()
        while True: # Loop until a valid choice is made
            choice = await_choice(
                question=(
                f"{pr.colours['green']}What do you play with?\n"
                f"{pr.colours['cyan']}(1: "+pr.colours["green"]+"computer"+pr.colours["cyan"]+") I'll play with the computer!\n"
                "(2: "+pr.colours["green"]+"bookshelf"+pr.colours["cyan"]+") I'll read a book!\n"
                "(3: "+pr.colours["green"]+"window"+pr.colours["cyan"]+") I'll look out the window!"
                ),
                string="I'll... "
            )
            # Starts a branching path of responses. Always ends with the same result, Just events in the environment around the player
            # No need to track which ones have been done. Player only gets the chance to use 1.
            if "computer" in choice or "pc" in choice or choice == "1":
                pr.delay(
                    text="You walk with haste over to the computer, and sit down in the chair.",
                    delay=0.05,
                    colour="cyan"
                )
                sleep()

                while True:
                    try:
                        object_choice = await_choice(
                            question="What do you play?",
                            string="I'll play... "
                            )
                        
                        if object_choice == "" or object_choice == " ":
                            raise TypeError("No input given")

                        break # Breaks the loop if a valid choice is made
                    except TypeError:
                        continue

                pr.delay(
                    text="You turn on the computer, and start playing "+object_choice+", The characters are great! They're.. compassionate!",
                    delay=0.05,
                    colour="cyan"
                )
                sleep()
                pr.delay(
                    text="... The way they speak reminds me of dad... I.. miss him..",
                    delay=0.1, print_faster=("I... ", 0.6),
                    colour="cyan"
                )
                sleep(5)
                pr.delay(
                    text="Tears start to well up in my eyes, and I start to cry..",
                    delay=0.1, colour="blue"
                )
                sleep()
                pr.delay(
                    text="You hear the door open behind you, and I quickly wipe my tears away.",
                    delay=0.05, colour="blue"
                )
                sleep(1)
                pr.delay(
                    text="Mum can't know I still think about him.. She'll be crushed..",
                    delay=0.05, colour="blue", print_faster=("She'll be crushed..", 0.2)
                )
                sleep()
                pr.partial_solid(
                    text="You put on your best smile, turn around to see mum standing in the doorway, with a smile on her face.",
                    default_colour="cyan", targets=["You put on your best smile"], target_colours=["yellow"]
                )
                break
            elif "book" in choice or choice == "2":
                pr.delay(
                    text="You walk over to the bookshelf, and look at the books on the shelf.",
                    delay=0.05, colour="cyan"
                )
                sleep()
                pr.delay(
                    text="I wonder which one I should read..",
                    delay=0.05, colour="cyan"
                )
                while True:
                    try:
                        object_choice = await_choice(
                            question="Which book do you read?",
                            string="I'll read.. "
                            )
                        
                        if object_choice == "" or object_choice == " ":
                            raise TypeError("No input given")

                        break # Breaks the loop if a valid choice is made
                    except TypeError:
                        continue

                # No specific books to choose. it just gets the name of the book to enter in
                pr.delay(
                    text="You pick up the book "+object_choice+" and start reading.",
                    delay=0.05, colour="cyan"
                )
                sleep(6)
                pr.delay(
                    text="You say \"Maybe I should've picked something else.. this.. reminds me of him..\"",
                    delay=0.05, colour="cyan", print_faster=("this..", 1)
                )
                sleep(3)
                pr.delay(
                    text="As you speak.. your voice chokes up..",
                    delay=0.05, colour="blue"
                )
                sleep(6)
                pr.delay(
                    text="Dad isn't coming back home..",
                    delay=0.2, colour="blue"
                )
                sleep()
                pr.delay(
                    text="I wipe my tears away.. I can't let mum see me like this..",
                    delay=0.05, colour="blue"
                )
                sleep()
                pr.delay(
                    text="I still have the happy memories! I'll be fine! Everything will be fine!",
                    delay=0.05, colour="blue"
                )
                sleep()
                pr.delay(
                    text="I hear the door open behind me, and I quickly wipe my tears away.",
                    delay=0.05, colour="blue"
                )
                break
            elif "window" in choice or choice == "3":
                pr.delay(
                    text="You walk over to the window, taking in the view outside.",
                    delay=0.05, colour="cyan"
                )
                sleep()
                pr.delay(
                    text="The birds are chirping, and children are playing in the distance.",
                    delay=0.05, colour="cyan"
                )
                sleep()
                pr.delay(
                    text="... Watching them play, I remember how dad used play board games with me... I.. wish he was here..",
                    delay=0.1, print_faster=("I.. ", 0.6),
                    colour="cyan"
                )

                while True:
                    try:
                        object_choice = await_choice(
                            question="What board game did you use to play outside?",
                            string="I'll used to play.. "
                            )
                        
                        if object_choice == "" or object_choice == " ":
                            raise TypeError("No input given")

                        break # Breaks the loop if a valid choice is made
                    except TypeError:
                        continue
                
                pr.delay(
                    text="I.. miss him.. I.. Miss how we used to play "+object_choice.lower()+" together.. I..",
                    delay=0.1, print_faster=("I.. ", 0.6),
                    colour="cyan"
                )
                sleep(5)
                pr.delay(
                    text="Tears start to run down my face, and I start to cry quietly..",
                    delay=0.1, colour="blue"
                )
                sleep()
                pr.delay(
                    text="Suddenly, I hear the door creak open behind me, and I quickly dry my eyes.",
                    delay=0.05, colour="blue"
                )
                sleep(1)
                pr.delay(
                    text="Mum shouldn't see me like this.. It would break her heart..",
                    delay=0.05, colour="blue", print_faster=("It would break her heart..", 0.2)
                )
                sleep()
                pr.partial_solid(
                    text="I force a smile onto my face, turn around to see mum standing in the doorway, looking at me with a gentle smile.",
                    default_colour="cyan", targets=["I force a smile onto my face"], target_colours=["yellow"]
                )
                break
            else:
                continue

        sleep(5)
        pr.delay(
            text="\"I'm sorry for taking so long "+get("player.name")+"! I hope you weren't too bored!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        if "computer" in choice or "pc" in choice or choice == "1":
            pr.delay(
                text="\"I wasn't!~ I was just watching some.. streamers online! They're really funny!\" You say",
                delay=0.05, colour="cyan"
            )
        elif "book" in choice or choice == "2":
            pr.delay(
                text="\"I wasn't!~ I was just reading a.. book! It's fun!\" You say",
                delay=0.05, colour="cyan"
            )
        elif "window" in choice or choice == "3":
            pr.delay(
                text="\"I wasn't!~ I was just.. looking out the window! It's a nice day!\" You say",
                delay=0.05, colour="cyan"
            )
        sleep()
        pr.delay(
            text="\"That's good!~ I'm glad you're having fun!\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep(5)
        pr.delay(
            text="Now, \"I have a surprise for you!\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Close your eyes "+get("player.name")+"!\" She says with glee, and so you do",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Now open them up!\" She says",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You open your eyes, and as you do, you see her holding 2 tickets in her hand to a \""+object_choice+"\" convention",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"I know how much you love "+object_choice+"! So I thought we could go together!\" She says cheerfully",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"I.. I love it! Thank you mum!\" You say, hugging her",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="She hugs you back, and says \"I love you too!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You feel warm and happy, and you smile to yourself",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Now, get some rest, we leave tomorrow morning!\" She says, and you nod your head. You walk back to your room, and get into bed.",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You close your eyes, and drift off to sleep, excited for tomorrow.",
            delay=0.05, colour="cyan"
        )
        sleep(8)
        pr.delay(
            text="...",
            delay=3, colour="cyan"
        )
        sleep(3)
        pr.delay(
            text="You wake up, and look around your room, messy, littered with toys..\nA Surreal and cheerful feeling washes over you!",
            delay=0.05, colour="cyan"
        )
        sleep(3)
        pr.delay(
            text="You jump out of bed! Giggling as the new day starts to unfold and get dressed for the day! I feel so excited! I can't wait to go to the convention!",
            delay=0.05, colour="cyan"
        )
        sleep(3)
        pr.delay(
            text="You run to the door, Just before you open it, mum opens it from the other side, and says \"Good morning!~ I could hear your already awake!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Good morning!~\" You say, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Are you excited for today?\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Yes! I can't wait to go to the convention!\" You say, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"I'm glad!~ I'm excited too! Now lets get going, your ready right?\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Yes! I'm ready!\" You say, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Great! Lets go!\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep(5)
        pr.solid_colour(
            text=(
            "\n\nYou walk out the door, and head to the car, and get in, and buckle up."
            "\nYou look out the window, and see the sun shining through the trees, and the birds chirping.\n"
            "\n... 10 minutes pass, You arrive!...\n"
            ),
            colour="cyan"
        )
        await_choice("Press enter to continue...")
        return object_choice
    
    def p2():
        pr.partial_solid(
            text="You run out of the car, and into the convention center, and look around, and see a sign that says \""+get("endings.c0.p2.object_choice")+"\" convention",
            targets=["\""+get("endings.c0.p2.object_choice")+"\" convention"],
            target_colours=["green"],
            default_colour="cyan"
        )
        sleep()
        pr.delay(
            text="You run over to the sign, and see a long line of people waiting to get in, and you get in line, and wait for a while.\nThis place is packed!",
            delay=0.08, colour="cyan"
        )
        sleep(5)
        pr.delay(
            text="Mum catches up behind me, she says \""+get("player.name")+"! You absolutely cannot run off like that!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"I'm sorry mum! I was just excited!\" You say, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"I know! But you still can't run off like that!\" She says, smiling as she chuckles",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You smile back, and say \"Okay! I won't!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Good!\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You wait in line for a while, and eventually get to the front, and the person at the front says \"Tickets please!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text=(
            "Mum hands them the tickets, and they say \"Alright! Enjoy the convention!\"\n"
            "Hah! Here we go!"
            ),
            delay=0.05, colour="cyan"
        )
        sleep(5)
        pr.delay(
            text="You walk into the convention center, and look around, and see a lot of people, and a lot of booths, and a lot of games, books and board games!",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You run over to the first area you see, mum following close behind, and see an \""+get("endings.c0.p2.object_choice")+"\" Booth!",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You say to yourself \"I love this! I wonder if they have anything new!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You look at the booth, they have a pendant from "+get("endings.c0.p2.object_choice")+".. You fixate on it for a little bit..",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="Mum observes me looking at it, and says \"Would you like it?\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="You jump a little from the shock of having your focus broken, you say \"Y-Yeah! I w-would!\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="\"Alright!~\" She says, smiling",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="She walks over to the booth, and buys the pendant, and she gets on her knees and put it around your neck..",
            delay=0.05, colour="cyan"
        )
        add_data(key="player.inventory.items", value="\""+get("endings.c0.p2.object_choice")+"\" pendant")
        sleep(5)
        pr.delay(
            text="You say \"Thank you mum!\" and I give her a hug",
            delay=0.05, colour="cyan"
        )
        sleep()
        pr.delay(
            text="She smiles and gives me a hug and says \"You're welcome!~\"",
            delay=0.05, colour="cyan"
        )
        sleep()
        await_choice("Press enter to continue...")
        clear_console()
        incident_text = f"{locget('the_incident.name')}\n{locget('the_incident.description')}\n\n"
        pr.delay(
            text=incident_text+"Suddenly, you hear a loud noise.. And another one.. and another.. your ears start to ring..",
            delay=0.2, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"You look around, and see a lot of people running around, and screaming...\nMum looks terrified, she's covering most of you.. you can't see whats happening anymore...",
            delay=0.1, colour="cyan", print_faster=("Mum looks terrified, she's covering most of you.. you can't see whats happening anymore...", 0.1)
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"Suddenly, more loud sounds.. People fall to the ground.. Covered in red.. and mum is dragging you by your wrist away.. I cant see her face! Why is everyone scared?!",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+get("player.name")+"! Honey, its going to be okay! We just need to get out of here!\" She says, terrified.. Why is she scared!?",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"You hear more loud sounds, and more people fall to the ground.. Why are they falling? Why are they covered in red?",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"Your mum looks around corner, she says \""+get("player.name")+" Lets go! Its.. l-like a game!\"\n She says, terrified.. What's happening??",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"You run with her, and you hear more loud sounds.. and more people fall to the ground..",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"You run with her, and you hear more loud sounds.. and more people fall to the ground..\nSuddenly...",
            print_faster=("Suddenly...", 0.3), delay=0.1, colour="cyan"
        )
        await_choice("")
        pr.delay(
            text=incident_text+"You hear a loud sound.. and you feel a sharp pain in your chest.. and you fall to the ground.. The sounds of your mum screaming.. Did I do something wrong?",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"You hear more loud sounds.. Mum is crying.. Suddenly.. I see my mum.. She's covered in red now.. She says.. \""+get("player.name")+"... I-I'm s-so sorry..\"",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"She's.. not moving.. Why.. Why is she not moving?",
            delay=0.1, colour="cyan"
        )
        await_choice("")
        clear_console()
        pr.delay(
            text=incident_text+"I feel cold.. and tired.. I.. I can't move.. I.. I can't see.. I.. I can't hear..",
            delay=0.1, colour="cyan"
        )
        sleep(20)
        pr.delay(
            text=incident_text+"... Mum?",
            delay=1, colour="cyan"
        )
        return True