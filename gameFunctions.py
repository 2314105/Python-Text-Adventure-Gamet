import os
import random
import time

import gameClasses

border = ("\n<------------------------------------------------------------------------------------------>\n")

# Clears screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
#Prompts the user to input to clear the screen
def pressEnterToContinue():
    input("press enter to continue ...")
    clear()

def menu():
    while True:
        clear()
        print(f"{border}\n\t\t\tThe Hero of Umaros and the Giant Behemoth\n{border}\n"
              "\n1. New Game\n"
              "\n2. Load Game\n"
              "\n3. Help\n"
              f"\n4. Quit\n\n{border}\n")
        
        command = input("Type thy choice: \n\n").lower()

        if command == "1" or command == "new game" or command == "one":
            break

        elif command == "2" or command == "load game" or command == "two":
            loadGame()
            break

        elif command == "3" or command == "help" or command == "three" or command == "h":
            help()
            
        elif command == "4" or command == "quit" or command == "four" or command == "q":
            quitGame()
            break 

#Yes or no question
def yeaOrNay(prompt):
    while True:
        userInput = input(prompt).lower()
        if userInput in ["yes", "y", "yea"]:
            return True
        elif userInput in ["no", "n", "nay"]:
            return False
        else:
            print("Invalid input. Please enter Yea or Nay.")
        

def menu(ui):
    while True:
        clear()
        print(ui.textLoopBorder("\n\t\t\tThe Hero of Umaros and the Giant Behemoth\n\n"
              "\n1. New Game\n"
              "\n2. Load Game\n"
              "\n3. Help\n"
              "\n4. Quit\n\n\n"))
        
        command = input("Type thy choice: \n\n").lower()

        if command == "1" or command == "new game" or command == "one":
            break

        elif command == "2" or command == "load game" or command == "two":
            loadGame()
            break

        elif command == "3" or command == "help" or command == "three" or command == "h":
            help()
            
        elif command == "4" or command == "quit" or command == "four" or command == "q":
            quitGame()
            break 

def introduction():
    clear()
    print(f"{border}introduction{border}"
          "\nAmidst the mystical realm of Umaros, where tales of valor echo through the ages, you "
          "\nstand as a celebrated hero. The villagers sing songs of your past triumphs, and your "
          "\nname is synonymous with bravery and honor. However, a shadow looms over the "
          "\npeaceful village of Mentos, as the ancient giant Behemoth unleashes his wrath upon its "
          "\nunsuspecting dwellers."
          "\n"
          "\nThe once-thriving village now trembles in the face of Behemoth's malevolence, and a "
          "\ndesperate call for aid reaches your ears. As the hero of Umaros, duty calls you to "
          "\nembark on a perilous quest to rescue the besieged village and thwart the ancient "
          "\ngiant's rampage."
          f"\n\nPart 1/2\n{border}")
    pressEnterToContinue()
    
    print(f"{border}introduction{border}"
          "\nBehemoth's icy castle, a foreboding structure in the distant mountains, stands as the"
          "\nepicenter of the turmoil. To reach the heart of the storm and confront the colossal "
          "\nadversary, you must first unravel a cryptic riddle guarding the castle's entrance. Inside, "
          "\na critical artifact awaits – the key to Behemoth's throne room, where the fate of Mentos "
          "\nhangs in the balance."
          "\n"
          "\nYour mission is clear: vanquish the ancient giant, restore peace to the village of "
          "\nMentos, and etch your name further into the annals of Umaros as a true hero. As you "
          "\nstand at the precipice of this epic journey, the time has come to choose your path. Will "
          "\nyou wield the arcane powers of a Mage, the unyielding strength of a Warrior, or the "
          "\ncunning finesse of a Rogue? The destiny of Umaros rests in your hands. Choose wisely "
          "\nand embark on your quest to secure victory and glory."
          f"\n\nPart 2/2\n{border}")
    pressEnterToContinue()
    
    
def loadGame():
    clear()
    print("loagGame")
    
def quitGame():
    clear()
    print("Farewell, brave adventurer! Until we meet again.")
    return "quit"


def help():
    clear()
    print(f"{border}\nHelp\n{border}\n\n"
          "\nType: help or h to open the instructions menu"
          "\n"
          "\nType: quit or q to quit the game"
          "\n"
          "\nType: stats or s to show your charcters stats"
          "\n"
          "\nType: north, east, south or west for moving across rooms"
          "\n"
          "\nType the corrsponding number to what you would like to do"
          "\n")
    
    pressEnterToContinue()

    
def getPlayerName():
    while True:
        clear()
        playerName = input("Tell me Hero, what is thy Name?\n: ").capitalize()
        if 3 <= len(playerName) <= 10:
            confirmName = yeaOrNay(f"{border} Is {playerName} your Name Yae/Nay: \n\n")
            if confirmName:
                return playerName
        else:
            print("Invalid name length. Your name should be between 4 and 10 characters.")
    
def displayRoomInformation():
    clear()
    print(f"{border}"
          f"{currentRoom["location"]}"
          f"{border}"
          "\nCurrent Room Description:\n"
          f"\n{currentRoom["description"]}")
    
    if currentRoom ["item"]:
        print(f"\nIn the {currentRoom["location"]} you see a key item: {currentRoom["item"]}{border}")
    else:
        print(border)
    
def characterCreation():
    playerName = getPlayerName()
    player = None
    
    while True:
        clear() 
        print(f"{border}Pick a character: \n\n1. Warrior\n\n2. Mage\n\n3. Rogue{border}")
        
        while True:
        
            playerChoice = input(f"Type thy choice: \n").lower()
            
            if playerChoice == "1" or playerChoice == "warrior" or playerChoice == "one":
                player = Ccharacter(playerName, "Warrior", 100, 20, 15, {"Double Strike": 20}, {"health potion": 30, "Shield": 10})
                break
            elif playerChoice == "2" or playerChoice == "mage" or playerChoice == "two":
                player = Ccharacter(playerName, "Mage", 60, 60, 10, {"Magic Dart": 15, "Magic Arrow": 30}, {"Mana potion": 20, "Robe": 8})
                break
            elif playerChoice == "3" or playerChoice == "rogue" or playerChoice == "three":
                player = Ccharacter(playerName, "Rogue", 70, 40, 12, {"Backstab": 25}, {"Smoke bomb": 8, "Cloak": 8})
                break
            else:
                print("Try again")
                pressEnterToContinue()

        player.showStats()

        userSelection = yeaOrNay(f"{border} Is this your class Yae/Nay: \n\n")
        if userSelection:
            return player
        
def takeItem(currentLocation, ui):
    success = False
    for item in currentLocation.items:
        currentLocation.removeItem(item)
        success = True
        break
    if success:
        print(ui.textLoopBorder(f"You picked up {item}\n"))
        pressEnterToContinue()
    else:
        print(ui.textLoopBorder("Command not recognized"))