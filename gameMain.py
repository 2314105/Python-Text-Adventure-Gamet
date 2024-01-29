#Import librarys
import os
import random
import time

asciiArtFilePath = "AskiiArt.txt"

#Character class
class CCharacter:
    # Initialize character attributes
    mName = ""
    mHero = "" 
    mHealth = ""
    mKeys = ""
    mDamage = ""
    mDefence = ""
    mInventory = ""
    mScore = ""
    mFirstLine = ""
    mLastLine = ""

    def __init__(self, name, hero, health, key, damage, defence, inventory, score, firstLine, lastLine):
        # Constructor to initialize character attributes
        self.mName = name
        self.mHero = hero
        self.mHealth = health
        self.mKeys = key
        self.mDamage = damage
        self.mDefence = defence
        self.mInventory = inventory
        self.mScore = score
        self.mFirstLine = firstLine
        self.mLastLine = lastLine

    # Calls Askii art from text file and displays art based on the lines from the constructors
    def AskiiArt(self):
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[self.mFirstLine-1:self.mLastLine-1]:
                print(line.rstrip())

    #Displays players stats
    def playerStats(self):
        clear()
        self.mDefence = round(self.mDefence,2)
        self.AskiiArt()
        print(f"{border}Name: {self.mName}{border}"
              f"Score:_________ {self.mScore}"
              f"\nClass:_________ {self.mHero}"
              f"\nHP:____________ {self.mHealth}"
              f"\nAttack:________ {self.mDamage}"
              f"\nDeffence:______ {self.mDefence}%{border}"
              f"Inventory:_____ {self.mInventory}"
              f"\nKeys:__________ {self.mKeys}{border}")
        
    #Adds items to inventory
    def addToInventory(self, item):
        self.mInventory.append(item)
        print(f"{item} added to inventory.")

    #Uses item from inventory, adds it to stats and removes it from list
    def useItem(self):
        # Initilize potion effects
        healthEffect = 30
        damageEffect = 15
        defenceEffect = 0.1
        boosterHealthEffect = 5
        boosterDamageEffect = 5
        boosterDefenceEffect = 5

        clear()
        command = input(f"\n{border}\nWhat item would you like to use\n{border}\nInventory: {self.mInventory}\n{border}\n>").lower()
        if command in ["health", "health potion", "h"]:
            if "health potion" in self.mInventory:
                self.mHealth += healthEffect
                self.mInventory.remove("health potion")
                print("Your health has increased by 30 points")
        elif command in ["damage", "damage potion", "d"]:
            if "damage potion" in self.mInventory:
                self.mDamage += damageEffect
                self.mInventory.remove("damage potion")
                print("Your physical damage have increased by 14 points")
        elif command in ["protection", "protection potion", "p"]:
            if "protection potion" in self.mInventory:
                self.mDefence += defenceEffect
                self.mInventory.remove("protection potion")
                print("Your protections have increased by 0.05%")
        elif command in ["boost","booster", "booster potion", "b"]:
            if "booster potion" in self.mInventory:
                self.mDefence += boosterDefenceEffect
                self.mDamage += boosterDamageEffect
                self.mHealth += boosterHealthEffect
                self.mInventory.remove("booster potion")
                print(f"All Your stats have increased by 5 and defence by 0.05%")
        else:
            print(f"{command} not recognised.")
            pressEnterToContinue()

# Rooms class
class CRoom:
    #Initilize room attributes
    mLocation = ""
    mDescription = ""
    mDirections = ""
    mChallenge = ""
    mItem = ""
    mFirstLine = ""
    mLastLine = ""

    def __init__(self, location, description, directions, challenge, item, firstLine, lastLine):
        # Constructor to initialize room attributes
        self.mLocation = location
        self.mDescription = description
        self.mDirections = directions
        self.mChallenge = challenge
        self.mItem = item
        self.mFirstLine = firstLine
        self.mLastLine = lastLine
        
    def AskiiArt(self):
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[self.mFirstLine-1:self.mLastLine-1]:
                print(line.rstrip())

    # Displays the current rooms description
    def displayLocationDescription(self):
        self.AskiiArt()
        print(f"\n{border}\nLocation: {self.mLocation}\n{border}\n{self.mDescription}\n{border}")
        if self.mChallenge["completed"]:
            print(f"Challenge completed{border}")
        else:
            print(f"Challenge not completed{border}")

    # Navigate rooms
    def navigation(self, direction, playerCharacter):
    # Checks if the rooms challenge has been completed
        if self.mChallenge and not self.mChallenge["completed"]:
            print("You must complete the challenge before moving to the next room")
            pressEnterToContinue()
            return self
        # Checks of the next room is the boss room and if you have all 4 keys
        elif direction in self.mDirections:
            nextRoomName = self.mDirections[direction]
            nextRoom = rooms[nextRoomName]
            if nextRoomName == "hiddenRituralSite":
                if len(playerCharacter.mKeys) == 4:
                    return nextRoom
                else:
                    print(f"NEB: Hey {playerCharacter.mName}, you need all four runes to enter there... stupid")
                    pressEnterToContinue()
                    return self
            else:
                return nextRoom
        else:
            pressEnterToContinue()
            return self

# Define rooms using the CRoom class
rooms = {
    "enchantedForest": CRoom(
        location = "Enchanted Forest",
        description ="You're surrounded by tall dark trees, which are filled with magical energy."
        "\nThe leaves fall leaving a blue haze in the air, connecting to each other like a dance,"
        "\nenchanting any who watch this magical play of nature. The ground glows from the icy blue"
        "\nleaves. You see footsteps that only lead into the castle but none that lead away;"
        "\n not all of the footsteps are human.",
        directions = {"west": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "Enchanted Rune",
        firstLine = 216,
        lastLine = 238),

    "frozenStoneGarden": CRoom(
        location = "Frozen Stone Garden",
        description = "Frozen figures are every where, perfectly sculpted with fine and intracet"
        "\ndetails, but at a closer inspection you come to find that the sculptures are people,"
        "\nbeasts and monsters who have been trapped here for generations. Amongst the statues"
        "\nyou see a familia face, a mystical nome called Neb. they say when nomes die they tend"
        "\nto haunt the surrounding area, best be carful.",
        directions = {"north": "floodedAlcemyRoom", "east": "enchantedForest", "south": "magicalLibariy", "west": "hiddenRituralSite"},
        challenge = {"completed": False},
        item = "Ice Rune",
        firstLine = 238,
        lastLine = 275),

    "floodedAlcemyRoom": CRoom(
        location = "Flooded Alcemy Room",
        description = "Vivid hues of moss and slime coat the walls, creating a surreal tapestry of colors. The floor,"
        "\nobscured by an unseen flood, bears witness to a chemical concoction that has transformed the"
        "\nenvironment into a mesmerizing yet mysterious spectacle. The mixture of diverse chemicals"
        "\nbeneath contributes to a uniquely vibrant and alluring atmosphere.",
        directions = {"south": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "Liqued Rune",
        firstLine = 275,
        lastLine = 293),

    "magicalLibariy": CRoom(
        location = "Magical Libariy",
        description = "A whirlwind of books fills the air, with each tome rising from a pile on the ground,"
        "\nfloating gracefully to find its place on an infinite bookcase. Yet, the cycle repeats as"
        "\nthe books descend, creating a mesmerizing and perpetual dance of literature. The never-ending"
        "\nspectacle captures the essence of an unending cycle, where knowledge and stories take flight"
        "\nonly to return and continue their enchanting journey.",
        directions = {"north": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "Magic Rune",
        firstLine = 293,
        lastLine = 324),

    "hiddenRituralSite": CRoom(
        location = "Hidden Ritural Site",
        description = "As you tread through the secretive ceremonial grounds, an unexpected revelation unfolds—the\nimposing Boss emerges from the shadows. This pivotal encounter marks a turning point,\npromising both challenges and profound revelations within the mysterious heart of this\nconcealed sanctuary.",
        directions = {"east": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "boss key",
        firstLine = 324,
        lastLine = 355)}

#border for UI
border = ("\n<==========================================================================================>\n")  

# Introduction
def introduction(playerCharacter):
    clear()
    print(f"{border}Introduction{border}")
    print(f"Greetings {playerCharacter.mName}, you are the hero sent from the kingdom Umaros tasked with saving the"
        "\nvillage of Mentos. They are currently under tyrnical rule of a giant known mostly as behmoth"
        "\nit's also been rumed that he now has a dragon under his command so please be carfule in"
        "\nyour future conquest. The icy castle is full of traps and riddles, any time an adventurer"
        "\nhas gone there its been diffrent every time and you cant leave the room until the"
        "\nchallenge has been complete, so stay vigilant and be aware of your surroundings")
    pressEnterToContinue()    

# Clears screen
def clear():
    os.system('cls')

# Prompts the user to input to clear the screen
def pressEnterToContinue():
    input("press enter to continue ...")
    clear()

# Yes or no question
def yeaOrNay(prompt):
    while True:
        userInput = input(prompt).lower()
        if userInput in ["yes", "y", "yea"]:
            return True
        elif userInput in ["no", "n", "nay"]:
            return False
        else:
            print("Invalid input. Please enter Yea or Nay.")

# Displays game over screen
def gameOver(playerCharacter):
    if playerCharacter.mHealth < 1:
        pressEnterToContinue()
        print(border)
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[201:208]:
                print(line.rstrip())
        print(f"{border}Score = {playerCharacter.mScore}{border}")
        print("\nTry Again?\n\n")
        command = yeaOrNay("Yae/Nay: \n\n>")
        if command:
            True
        else:
            quitGame()

# Gets players name and makes sure its not too long or too short
def characterName():
    while True:
        clear()
        name = input(f"{border}\nTell me Hero, What is thy Name? (3 and 10 characters)\n{border}\n\n>").capitalize()
        if 3 <= len(name) <= 10:
            confirmName = yeaOrNay(f"{border} Is {name} your Name Yae/Nay: \n\n")
            if confirmName:
                return name
            
# Lets player choose what character to play as
def characterCreator():
        name = characterName()
        while True:
            clear()
            while True:
                command = input(f"{border}\n{name}, What type of hero are you?\n{border}\n1. warrior (easy)\n\n2. mage (medium)\n\n3. rogue (hard)\n\n>").lower()
                if command in ["warrior", "one", "1"]:
                    character = CCharacter(name, "Warrior", 200, [], 20, 0.30,["protection potion"], 0, 97, 123)
                    break
                elif command in ["mage", "two", "2"]:
                    character = CCharacter(name, "Mage", 150, [], 25,0.25, ["booster potion"], 0, 76, 97)
                    break
                elif command in ["rogue", "three", "3"]:
                    character = CCharacter(name, "Rogue", 130, [], 30, 0.20, ["damage potion"], 0, 123, 143)
                    break
            character.playerStats()
            if character.mHero == "Warrior":
                 print("The Warrior is the easiest of the three classes, with a high health pool, high \nphysical damage and a strong defence makes then ideal for your first play through.\n")
            elif character.mHero == "Mage":
                print("The Mage is a medium diffculty class, if you're looking for a bit of a challenge and \nwant to weild the arcane arts pick mage.\n")
            else:
                print("The Rogue class is the hardest out of all three, if youre feeling lucky you can get \nsome series damage out, but ifyour hit its gunna hurt.\n")
                
            command = yeaOrNay("Is this your class Yae/Nay: \n\n>")
            if command:
                return character
            
# Random enemy generator
def randomEnemySelector(currentRoom):
    randomEnemy = random.randint(0,4)
    # Checks if boss room then returns boss else you get a random enemy
    if currentRoom.mLocation == "Hidden Ritural Site" and currentRoom.mChallenge["completed"] == False:
        enemy = CCharacter("boss", None, 100, None, 30, 0.3, None, 500, 1, 29)
        return enemy
    elif randomEnemy == 1:
        enemy = CCharacter("Gobblin", None, 40, None, 12, 0.10, None, 100, 162, 184)
        return enemy
    elif randomEnemy == 2:
        enemy = CCharacter("Demon", None, 40, None, 18, 0.25, None, 130, 29, 54)
        return enemy
    elif randomEnemy == 3:
        enemy = CCharacter("Lizard Man", None, 50, None, 16, 0.12, None, 150, 144, 162)
        return enemy
    elif randomEnemy == 4:
        enemy = CCharacter("Manticore", None, 70, None, 20, 0.28, None, 200, 54, 76)
        return enemy
    
# Random loot drops
def loot(playerCharacter):
    loot = ["health potion", "damage potion", "protection potion", "booster potion"]
    lootChance = random.randint(0,3)
    lootDropped = loot[lootChance]
    playerCharacter.addToInventory(lootDropped)
    return lootDropped

# Starting Main menu
def menu():
    while True:
        clear()
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[0:29]:
                print(line.rstrip())
        print(f"{border}\n\t\t\tThe Hero of Umaros and the Giant Behemoth\n{border}"
              "1. New Game\n"
              "2. Load Game\n"
              "3. Help\n"
              f"4. Quit{border}")
        command = input("Type thy choice:\n\n> ").lower()
        if command == "1" or command == "new game" or command == "one":
            return True
        elif command == "2" or command == "load game" or command == "two":
            loadGame()
            return False
        elif command == "3" or command == "help" or command == "three" or command == "h":
            help()
        elif command == "4" or command == "quit" or command == "four" or command == "q":
            quitGame()
            return False
        
# Allows the player to load a game save
def loadGame():
    clear()
    print("loagGame")

# Allows the player to exit the game
def quitGame():
    clear()
    print("Farewell, brave adventurer! Until we meet again.")
    return "quit"

# Allows the player to recieve additional help
def help():
    clear()
    print(f"{border}\nHelp\n{border}\n\n"
    "General:\nType: help or h to open the instructions menu\nType: quit or q to quit the game\nType use item or u to check your inventory and use an item\nType: stats or s to show your charcters stats\nType: north, east, south or west for moving across rooms"
    "\n\nCombat:\nType: attack, a or just pressing enter will allow you to attack\nrunning away will give the enemy a chance to to get a hit in\n typing U will allow you tu use a item mid fight"
    "\n\nRiddle:\nType: tip or t will give you a hint for th riddle\n")
    pressEnterToContinue()

# You win Screen 
def youWin(playerCharacter):
    clear()
    print(border)
    with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[208:215]:
                print(line.rstrip())
    print(f"\n{border}\nCongratulations {playerCharacter.mName} You've WON!!!\n{border}\n Here is your over all Score {playerCharacter.mScore}\n\n would you like to play again?\n\n")
    pressEnterToContinue()
    command = yeaOrNay("Yae/Nay: \n\n>")
    if command:
        menu()
    else:
        quitGame()

# Calls current room and displays information with UI
def displayRoomInformation(currentRoom):
    clear()
    print(f"{border}"
          f"{currentRoom["location"]}"
          f"{border}"
          "\nCurrent Room Description:\n"
          f"\n{currentRoom["description"]}")
    print(border)

# Player vs Enemy combat
def combat(playerCharacter, currentRoom):
    command = ""
    enemy = randomEnemySelector(currentRoom)
    print(f"you see a {enemy.mName}\nYou have 3 options: ")
    while enemy.mHealth > 0 and playerCharacter.mHealth > 0:
        randomDamage = random.randint(0, 5)
        pressEnterToContinue()
        enemy.AskiiArt()
        print(f"{border}{playerCharacter.mName} {playerCharacter.mHealth} |  {enemy.mName}  {enemy.mHealth}{border}")
        command = input(f"a: attack\nr: Run away\nh: Help\nu: Use item\n\n>").lower()
        if command in ["help", "h"]:
            help()
        if command in ["use item", "u"]:
            playerCharacter.useItem()
        if command in ["attack","a", ""]:
            print(f"You swing your weapon at {enemy.mName}")
            hitChance = random.randint(0,10)
            if hitChance > 3:
                clear()
                enemy.AskiiArt()
                enemy.mHealth -= (playerCharacter.mDamage + randomDamage)
                print(f"succesful strike, enemy Health is now{enemy.mHealth}")
                if enemy.mHealth > 0:
                    playerCharacter.mHealth -= round((enemy.mDamage + randomDamage) * playerCharacter.mDefence)
                    print(f"{enemy.mName} takes a swing and hits you, you now have {playerCharacter.mHealth}")
                    gameOver(playerCharacter)
                elif enemy.mHealth <= 0 and enemy.mName == "boss":
                    youWin(playerCharacter)
                else:
                    lootDropped = loot(playerCharacter)
                    playerCharacter.mScore += enemy.mScore
                    print(f"you have defeated the {enemy.mName}, it looks like it dropped somthing \nLoot: {lootDropped}\nScore: {playerCharacter.mScore}\n\n")
                    pressEnterToContinue()
                    break
            else:
                clear()
                print(f"your miss the {enemy.mName} leaving a opening for a counter attack")
                playerCharacter.mHealth -= (enemy.mDamage + randomDamage )
                print(f"{enemy.mName} landed a full damage hit,ignoring your deffence; current health is {playerCharacter.mHealth}")
                gameOver(playerCharacter)
        elif command in ["run away", "three", "3"]:
            clear()
            print("You try running away")
            hitChance = random.randint(0, 10)
            if hitChance > 3:
                print("You managed to escape")
                break
            else:
                print(f"You tried to escape but the {enemy.mName} was able to get you, Your Health {playerCharacter.mHealth}")
                playerCharacter.mHealth -= (enemy.mDamage + randomDamage)
                gameOver(playerCharacter)
        else:
            print(f"{command} not recognised")

def challenge(currentRoom, playerCharacter):
    if currentRoom.mChallenge and not currentRoom.mChallenge["completed"]:
        clear()
        print(f"A challenge in {currentRoom.mLocation} awaits you.")
        challengeType = random.choice(["riddle", "combat"])
        if currentRoom.mLocation == "Hidden Ritural Site":
            combat(playerCharacter, currentRoom)
        elif challengeType == "riddle": 
            riddle(playerCharacter)
        elif challengeType == "combat":
            combat(playerCharacter, currentRoom)
        playerCharacter.mKeys.append(currentRoom.mItem)
        currentRoom.mChallenge["completed"] = True
    else:
        print(f"The challenge in {currentRoom.mLocation} has already been completed.")

def randomRiddleSelector():
    randomRiddle = random.randint(1,4)
    if randomRiddle == 1:
        riddle = CCharacter("What cant speak, but will speak when spoken to?", ["echo", "a echo"], None, None,"I bounce of the walls", None, None, 120, 184, 202)
        return riddle
    elif randomRiddle == 2:
        riddle = CCharacter("The more of this there is, the less you see. What is it?", ["darkness", "night"], None, None,"Close your eyes what do you see", None, None, 120, 184, 202)
        return riddle
    elif randomRiddle == 3:
        riddle = CCharacter("A man dies of old age on his 25 birthday. How is this possible?", ["he was born on a leap year", "he was born on february 29","february 29", "leap year"], None, None,"Not every year has one", None, None, 120, 184, 202)
        return riddle
    elif randomRiddle == 4:
        riddle = CCharacter("I shave every day, but my beard stays the same. What am I?", ["barber", "hairdresser"], None, None,"you might visit them once or twice a month", None, None, 120, 184, 202)
        return riddle

def riddle(playerCharacter):
    command = ""
    riddle = randomRiddleSelector()
    while command != riddle.mHero:
        riddle.AskiiArt()
        print (f"{border}you hear an annoying voice...{border}NEB: if you want the key riddle me this: {riddle.mName}")
        command = input("What is your anwser?\n\nh: help\n\nt: tip\n\nl: leave\n\n>").lower()
        if command in ["help", "h"]:
            help()
        elif command in riddle.mHero:
            playerCharacter.mScore += riddle.mScore
            print(f"Well done {playerCharacter.mName} you guessed correctly")
            break
        elif command in ["tip", "t"]:
            print(f"ahh struggling are we, here this should help: \n\n>{riddle.mDamage}")
            pressEnterToContinue()
        elif command in["leave", "l"]:
            print("Couldnt handel it ayy, better luck next time")
            pressEnterToContinue()
            break
        else:
            print(f"{command} inccorect..\n")
    
def main():
    while menu():
        playerCharacter = characterCreator()
        introduction(playerCharacter)
        currentRoom = rooms["enchantedForest"]
        while playerCharacter.mHealth >= 0:
            clear()
            currentRoom.displayLocationDescription()
            userInput = input(f"\nType one of the following commands:\n\nChange room: {currentRoom.mDirections}\n\nL: Look\n\nS: Stats\n\nU: Use item\n\nH: Help\n\nE: Exit\n\n>").lower()
            if userInput in ["help", "h"]:
                help()
            elif userInput in ["look", "l"]:
                challenge(currentRoom, playerCharacter)
            elif userInput in ["stats", "s"]:
                playerCharacter.playerStats()
                pressEnterToContinue()
            elif userInput in ["use item", "u"]:
                playerCharacter.useItem()
            elif userInput in currentRoom.mDirections:
                currentRoom = currentRoom.navigation(userInput, playerCharacter)
            elif userInput in ["exit", "e"]:
                yeaOrNay("Are you Sure you want to  exit? (Y/N)")
                break
            gameOver(playerCharacter)
if __name__ == "__main__":
    main()

    