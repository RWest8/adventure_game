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

def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f"Sorry, the option {option} is invalid. Try again.")

def intro(item, aliens, weapon):
    print_pause(f"Good {greeting()} master Jedi!")
    print_pause("You are travelling in a galaxy far far away...")
    print_pause(f"When you are attacked by the " + aliens + "!")
    print_pause(f"Armed with your old trusty " + weapon + ".")
    print_pause("Do you want to fight back or continue your travels?")

def space(item, aliens, planet):
    if "super blaster 920 laser cannons" in item:
        print_pause("You are now back in space.")
        print_pause("And now...your ship is surrounded!")
        print_pause(f"The" + aliens + " are still out looking for a fight!")
    else:
        print_pause(f"You arrive on the planet " + planet + "." "The people\n"
                        "welcome you")
        print_pause("The popele inform you, your ship was attacked!")
        print_pause(f"The " + aliens + " are wreaking havoc in the universe.")
        print_pause(f"The people of " + planet + " retrofitted your ship with a\n"
                        "super blaster 920 laster cannons!")
        item.append("super blaster 920 laser cannons")
    command_center(item)

def fight(item, aliens):
    if "super blaster 920 laser cannons" in item:
        print_pause("You aim your cannons and fire one charge of your\n"
                    "super blaster 920 laser cannons!")
        print_pause(f"The " + aliens + " are blown to bits.")
        confirmation("YOU WIN")
    else:
        print_pause(f"You attack! The " + aliens + " hypersonic beams\n"
                    "pulverized your ship.")
        print_pause("Your are blown to bits.")
        confirmation("GAME OVER")

def command_center(item):
    choice = valid_input("Enter: yes or no: ", ["yes", "no"])
    if choice == "yes":
        fight(item, aliens)
    else:
        space(item)
    game_restart()

def game_restart():
    print_pause("\nWould you like to start another mission?")
    response = valid_input("Enter: yes or no: ", ["yes", "no"])
    if "yes" in response:
        print_pause("All Systems Initializing")
        print_pause("Starting Mission in")
        confirmation("321")
        play_jedi()
    elif "no" in response:
        print_pause(f"Okay. Good {greeting()} and Goodbye Master Jedi!")
    game_restart()

def play_jedi():
    item = []
    aliens = random.choice(["Pyke Boss", "Rancor", "Darth Sidious"])
    weapon = random.choice(["Lightsaber", "Tusken Raider rifle", "blaster"])
    planet = random.choice(["Tatooine", "Alderaan", "Naboo"])
    intro(item, aliens, weapon)
    command_center(item)

play_jedi()
