import time as t
import time
import sys 
import colorama
from colorama import Fore, Back, Style
colorama.init(convert=True)
# Blue_text = Fore.BLUE + 

# from ascii import*
# ascii = text2art("art")
# print(art)

reset_text=Style.RESET_ALL
print(Fore.BLUE,)
print(Fore.RED,)
print(Fore.YELLOW,)
print(Fore.GREEN,)

#winner function for criminal
def winner_criminal():
    delay_print("Congratulations my fellow hoodlum, when's the wedding?")
    delay_print("\nWould you like to play again? YES or NO?\n")
    new_game_criminal = input()
    if new_game_criminal == "yes":
       print("let's go again\n")
       intro()
    else:
       print("Maybe another time")

#winner function for police character
def winner_police():
    delay_print(f"{Fore.BLUE}Congratulations, you saved the day... and you didn't even have to kill anyone! You'll be running this station one day!")
    delay_print("Would you like to play again (YES OR NO)\n")
    new_game_police = input().upper()
    if new_game_police == "yes":
     print("lets go again\n")
     intro()
    else:
     print("Maybe another time")

# typewriter text example
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
        

#Intro Function
def intro():
    print("__        __   _                            \n\ \      / /__| | ___ ___  _ __ ___   ___  \n \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ \n  \ V  V /  __/ | (_| (_) | | | | | |  __/ \n   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  ")
    delay_print(f"{Fore.MAGENTA}\nIn a world, plagued with crime and depravity. Each of us has a choice to either stand in the way of crime. Or do we make a quick buck and add to it. Do you choose the role of the 'officer' or the 'offender'...\n\nTHE CHOICE IS YOURS!\n\n")
    time.sleep(1.5)
    delay_print("Type below 'officer' for the good guys OR 'offender' for the bad guys\n\n")
    
    character = input().lower()
    if character == "offender":
        criminal()
    elif character == "officer":
        police_officer()
    else:
        delay_print("Invalid Selection please choose 'officer' or 'offender'\n")
        intro()

#Entry question "back door" option
def back_door():
    # Added delays to stagger text adding some suspense to the printed strings
    t.sleep(1.5)
    delay_print(f"{Fore.BLUE}\nYou head around the building and see the fire exit, lucky for us the lock is broken and we proceed into the store, you get a view of the criminal holding the gun to the store owners head. how do you approach this situation?\n\n")
    t.sleep(1.5)
    delay_print("\n'A' - You put your persuasive talents to the test and calm the criminal with promises you will get him a pint if he puts the gun down...\n")
    t.sleep(1.5)
    delay_print("\nOR\n")
    t.sleep(1.5)
    delay_print("\n'B' - you take a necklace from the stand swing it around your head and charge at the criminal.\n\n")
    t.sleep(1.5)
    delay_print("\nType 'A' or 'B'\n")
    
    final = input().upper()
    if final == "A":
        winner_police()
    elif final == "B":
        delay_print(f"{Fore.BLUE}\nThe criminal turns the gun to you and fire's your vision begins to blur, you should of went for the donut after all\n\n")
        quit()
    else:
        delay_print("invalid answer, please choose either 'A' or 'B'")
        back_door()

# Entry question "smash through door" option
def smash_through_the_door():
    delay_print(f"{Fore.BLUE}\nThe criminal panics and stabs the store owner. Well done wise guy no wonder why nobody likes the police.")
    quit()

def optiona():
    delay_print(f"{Fore.BLUE}\nYou arrive at the scene of the crime, peering through the jewellery store window and see the suspect holding a gun, threatening the store owner. You notice he's wearing a 'make America great again' cap.\n\n")
    t.sleep(1.5)
    delay_print("\nYou're the cop how will you approach the situation?\n")
    t.sleep(1.5)
    delay_print("\n'A' - You can pull your pants up, take a deep breath and smash through the door, yelling FREEZE SUCKER!\n")
    t.sleep(1.5)
    print("\nOR")
    t.sleep(1.5)
    delay_print("\n'B' - Maybe there is a back door and we can creep through as the robber hasn't noticed us yet\n")
    t.sleep(1.5)
    delay_print("\nType 'A' or 'B'\n")
    t.sleep(1.5)
    option = input().upper()
    if option == "B":
        back_door()
    elif option == "A":
        smash_through_the_door
        quit()
    else:
        delay_print("Invlalid answer, please choose 'A' or 'B' genius...")
        optiona()

def optionb():
    delay_print(f"{Fore.BLUE}\nIt doesn't mean the end of the world it's just the beginning of a new game\n")
    

def police_officer():
    delay_print(f"{Fore.BLUE}\nCongratulations you've joined the good guys\n")
    t.sleep(1.5)
    print("                       _____________________\n    /  .       .      (<$$$$$$>#####<::::::>)\n   .      .     .  _/~~~~~~~~~~~~~~~~~~~~~~~~~\_   .       .   .   \ \n.(          . .  /~                             ~\ . .   .\n  ( . .        .~                                 ~.      .         )\n           ()\/_____                           _____\/()   .    .  ).\n(         .-''      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-.  ...\n.  . . .-~              __________________              ~-.  .    /\n .   ..`~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~'    . ) .\n    . .| | | #### #### || | | | [] | | | || #### #### | | | .\n   (   ;__\|___________|++++++++++++++++++|___________|/__;.   .\n     .  (~~====___________________________________====~~~)\n ( .  .. \------_____________[ POLICE ]__________-------/ ..  .     )\n         .  |      ||         ~~~~~~~~       ||      |\n             \_____/                          \_____/")
    delay_print("\nSuddenly a Call from HQ beckons from your police radio. A panic alarm has been pressed to report a robbery in a jewellery store on King Street. Now you have 2 options:\n")
    t.sleep(1.5)
    delay_print("\n'A' - You're a good officer after all, you take the call, turn on your engine and head on your way\n")
    delay_print("\nOR\n")
    t.sleep(1.5)
    delay_print("\n'B' - Sounds interesting, however Krispy Kreme's does have that new special donut you always wanted to try\n")
    t.sleep(1.5)
    delay_print("\nType 'A' or 'B'\n")
    option = input().upper()
    if option == "A":
        optiona()
    elif option == "B":
        optionb()
        quit()
    else:
        delay_print("\ninvalid answer, please choose either A or B to carry on with the game. Genius\n")
        t.sleep(1.5)
        police_officer()

#prints message to show user they have chosen the offender
def offender():
    delay_print(f"{Fore.RED}I see you've chosen the world of crime, make sure you don't get caught")

#Quit Function
def quit():
    # used ascii art to paste thr game over banner into the game
    print(f"{Fore.BLACK}\n\n┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n"
           "██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n"
           "██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n"
           "██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n"
           "███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n"
           "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n"
           "██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n"
           "██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n"
           "██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n"
           "███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n"
           "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼\n"
           "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
    #will print to the terminal allowing players to restart the game
    delay_print("Would you like to play again? (YES or NO)\n")
    playagain = input().upper()
    # YES will call the "Intro" function 
    if playagain == "YES": 
        delay_print("You got this!\n")
        # use this function to restart the "intro"
        intro() 
    else:
        delay_print("maybe next time! cya\n")
        
# Final Decision
def decision_time():
    t.sleep(1.5)
    delay_print(f"{Fore.RED}\nA - You walk over to the owner direct him to the jewellery stand, and make him open the case. demanding he give you the ring or you will blow his hobbit brains out\n")
    t.sleep(1.5)
    delay_print("\nOR\n")
    delay_print("\nB - You get really angry at the audacity of the store owner trying to press the silent alarm, you proceed to pistol whip him and mock him for his actions\n")
    t.sleep(1.5)
    delay_print("\nType 'A' or 'B'\n")
    decision = input().upper()
    if decision == "A":
        t.sleep(1.5)
        winner_criminal()
        
    elif decision == "B":
        t.sleep(1.5)
        delay_print("\nYou take to long giving the owner a hard time the shutters snap shut and you hear sirens in the distance. Its all over\n")
        quit()
    else:
        t.sleep(1.5)
        delay_print("\nYou must print A or B fool\n")
        decision_time()

# Weapon choice if jewellery store robbery option chosen
def weapon_choice():
    t.sleep(1.5)
    delay_print(f"{Fore.RED}\nchoose your weapon:\n\n")
    t.sleep(1.5)
    delay_print("\n'A' = Gun\n")
    print("\n+--^----------,--------,-----,--------^-,\n| |||||||||   `--------'     |          O\n`+---------------------------^----------|\n`\_,---------,---------,--------------'\n/ XXXXXX /'|       /'\n/ XXXXXX /  `\    /'\n/ XXXXXX /`-------'\n/ XXXXXX /\n/ XXXXXX /\n(________(                \n`------' ")
    t.sleep(1.5)
    delay_print("\nOR\n")
    t.sleep(1.5)
    delay_print("\n'B' = Knife\n")
    print("___________________________________ ______________________\n\                                  | (_)     (_)    (_)   \\ \n `.                                |  __________________   }\n   `-..........................____|_(                  )_/")
    weapon = input().upper()
    if weapon == "A":
        t.sleep(1.5)
        delay_print("\nYou're not taking any chances today. You immediately draw your gun and point it toward the small chaps head\n")
        t.sleep(1.5)
        delay_print("\nNice guys finish last, the owner begins to beg and plead for his life. You make your demands clear you want that big diamond ring over there. Suddenly the shutters close and jam leaving just enough space to wriggle out and escape. The owner has pressed the silent alarm time is of the essence, here's your chance what do you do?\n")
        t.sleep(1.5)
        decision_time()
    elif weapon == "B":
        t.sleep(1.5)
        delay_print("\nDutch courage takes over, you draw your knife and sway around. The hobbit rips his shirt to reveal his karate robes and black belt. He quickly delivers a swift side kick to the throat")
        t.sleep(1.5)
        delay_print("\nYou wake up gagging and handcuffed in the local hospital\n")
        t.sleep(1.5)
        quit()
    else:
        delay_print("\nYou must print A or B fool\n")
        t.sleep(1.5)
        weapon_choice()

# Criminal Start
def criminal():
    t.sleep(1.5)
    delay_print(f"{Fore.RED}\nI see you've chosen the world of crime, make sure you don't get caught\n")
    t.sleep(1.5)
    delay_print("\nYou said you'd bought a ring for your girlfriend, except you spent all your money on gambling and whisky\n")
    t.sleep(1.5)
    delay_print("\nYou have two options:\n")
    t.sleep(1.5)
    delay_print("\n'A' - bae is life, that jewellery store over there has some really nice rings, LETS ROB IT.\n")
    t.sleep(1.5)
    delay_print("\nor\n")
    t.sleep(1.5)
    delay_print("\n'B' - Use your last £1 to buy a cheap plastic ring from Poundland, true love is unconditional after all.\n")
    t.sleep(1.5)
    delay_print("\nType 'A' or 'B'\n")
    t.sleep(1.5)
    option = input().upper()
    if option == "A":
        delay_print("\nThere's no turning back now! You enter the store and check out the store owner he reminds you of Frodo Baggins from that movie with the ring, but you think you can take him, You have your trusty pocket knife or your gun, which do you choose?\n") 
        t.sleep(1.5)
        delay_print("\nYou have two options\n")
        t.sleep(1.5)
        weapon_choice()
    elif option == "B":
        t.sleep(1.5)
        delay_print("Crime, sometimes does pay\n")
        t.sleep(1)
        quit()
    else:
        t.sleep(1)
        delay_print("You must print A or B fool\n")
        t.sleep(1.5)
        criminal()  
    
intro()
#weapon_choice()

