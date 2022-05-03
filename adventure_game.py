import time
import random
from datetime import datetime


def greeting():
    if datetime.today().hour > 18:
        return("Evening")
    else:
        return("Day")
    print(greeting())

def confirmation(message):
    for n in range(len(message)):
        print(message[n])
        time.sleep(1)

def print_pause(statement):
    print(statement)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause(f"Sorry, the option {response} is invalid. Try again!")
    return response

def intro(item, aliens, weapon):
    print_pause(f"Good {greeting()} Master Jedi!")
    print_pause("You are travelling in a galaxy far far away...")
    print_pause(f"When you are attacked by the {aliens}!")
    print_pause(f"Armed with your old trusty {weapon}")
    print_pause("Do you want to fight back or continue your space odysey?")

def space(arsenal, aliens, planet):
    if "super blaster 920 laser cannons" in arsenal:
        print_pause("You are now back in space!")
        print_pause("And now... your ship is surrounded!")
        print_pause(f"The {aliens} are still out looking for a fight!")
    else:
        print_pause(f"You arrive in planet {planet} the people welcomes you!")
        print_pause("You are informed your ship was attacked!")
        print_pause(f"The {aliens} are wreaking havoc "
                    "in the universe!")
        print_pause(f"The people of {planet} "
                    "retrofitted your ship with a super blaster 920 "
                    "laser cannons!")
        arsenal.append("super blaster 920 laser cannons")
    command_center(arsenal)

def fight(arsenal, aliens):
    if "super blaster 920 laser cannons" in arsenal:
        print_pause("You aimed your cannons and fire one charge\n"
                    "of your super blaster 920 laser cannons!")
        print_pause(f"The {aliens} are blown bits and swallowed by "
                    "the black hole.")
        confirmation("YOU WIN")
    else:
        print_pause(f"You attack! but the {aliens} hypersonic beams\n"
                    "pulverized your ship before you can charge!!!")
        print_pause("You are blasted in Eternity!")
        confirmation("GAME OVER")

def command_center(arsenal):
    response = valid_input("Enter: yes or no\n", "yes","no")
    if "yes" in response:
        fight(arsenal, aliens)
    elif "no" in response:
        space(arsenal, aliens, planet)
    game_restart()

def game_restart():
    print_pause("\nWould like to restart another mission?")
    restart = valid_input("Enter your command:\n(1) yes\n(2) no\n", ['1','2'])
    if "1" in response:
        print_pause("All Systems Initializing")
        print_pause("Starting Mission in")
        confirmation("321")
        play_galacticx()
    elif "2" in response:
        print_pause(f"Okay Good {greeting()} and Goodbye Master Jedi!")
    game_resart()

def play_galacticx():
    item = []
    arsenal = []
    aliens = random.choice(["Pyke Boss", "Rancor", "Darth Sidious"])
    weapon = random.choice(["Lightsaber", "Tusken Raider rifle", "blaster"])
    planet = random.choice(["Tatooine", "Alderaan", "Naboo"])
    intro(item, aliens, weapon)
    command_center(arsenal)
    game_restart()

play_galacticx()
