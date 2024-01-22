#Import librarys
import os
import random
import time
#Character class
class CCharacter:
    def __init__(self, name, hero, health, keys, damage, defence, inventory, score):
        self.mName = name
        self.mHero = hero
        self.mHealth = health
        self.mKeys = []
        self.mDamage = damage
        self.mDefence = defence
        self.mInventory = inventory
        self.mScore = score
    #Displays players stats
    def playerStats(self):
        clear()
        self.mDefence = round(self.mDefence,2)
        print(f"{border}\nName: {self.mName}\n{border}"
              f"\nScore : {self.mScore}"
              f"\nClass: {self.mHero}"
              f"\nHP: {self.mHealth}"
              f"\nAttack: {self.mDamage}"
              f"\nDeffence: {self.mDefence}%\n{border}"
              f"\nInventory: {self.mInventory}"
              f"\nKeys: {self.mKeys}\n{border}")
    #Adds items to inventory
    def addToInventory(self, item):
        self.mInventory.append(item)
        print(f"{item} added to inventory.")
    #Uses item from inventory, adds it to stats and removes it from list
    def useItem(self):
        clear()
        command = input(f"\n{border}\nWhat item would you like to use\n{border}\nInventory: {self.mInventory}\n{border}\n>").lower()
        if command in ["health", "health potion", "h"]:
            if "health potion" in self.mInventory:
                self.mHealth += 30
                self.mInventory.remove("health potion")
                print("Your health has increased by 30 points")
        elif command in ["damage", "damage potion", "d"]:
            if "damage potion" in self.mInventory:
                self.mDamage += 15
                self.mInventory.remove("damage potion")
                print("Your physical damage have increased by 14 points")
        elif command in ["protection", "protection potion", "p"]:
            if "protection potion" in self.mInventory:
                self.mDefence += 0.1
                self.mInventory.remove("protection potion")
                print("Your protections have increased by 0.05%")
        elif command in ["boost","booster", "booster potion", "b"]:
            if "booster potion" in self.mInventory:
                self.mDefence += 0.05
                self.mDamage += 5
                self.mHealth += 5
                self.mInventory.remove("booster potion")
                print(f"All Your stats have increased by 5 and defence by 0.05%")
        else:
            print(f"{command} not recognised.")
            pressEnterToContinue()
 
# Rooms class
class CRoom:
    def __init__(self, location, description, directions, challenge, item):
        self.mLocation = location
        self.mDescription = description
        self.mDirections = directions
        self.mChallenge = challenge
        self.mItem = item
    # Displays the current rooms description
    def displayLocationDescription(self):
        print(f"\n{border}\nLocation: {self.mLocation}\n{border}\n{self.mDescription}\n{border}")
        if self.mChallenge["completed"]:
            print(f"Challenge completed{border}")
        else:
            print(f"Challenge not completed{border}")
            
    def navigation(self, direction, playerCharacter):
    # Checks if the room's challenge has been completed
        if self.mChallenge and not self.mChallenge["completed"]:
            print("You must complete the challenge before moving to the next room")
            pressEnterToContinue()
            return self
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
        description ="Surrounded by tall, dark trees, you stand in a mystical forest. Blue leaves gently descend\nfrom the sky, casting an ethereal glow upon the surroundings. The air is filled with\nenchantment as the magical foliage paints the scene with its serene illumination.",
        directions = {"west": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "Enchanted Rune"),
    "frozenStoneGarden": CRoom(
        location = "Frozen Stone Garden",
        description = "In this frigid landscape, an intense cold envelops everything. Frozen statues dot the\nsurroundings, revealing upon closer examination that they are not sculptures but the chilling\nfate of people and creatures caught in an icy stasis. The profound stillness of this frozen\nrealm conceals the silent stories of those who succumbed to the relentless grip of cold.",
        directions = {"north": "floodedAlcemyRoom", "east": "enchantedForest", "south": "magicalLibariy", "west": "hiddenRituralSite"},
        challenge = {"completed": False},
        item = "Ice Rune"),
    "floodedAlcemyRoom": CRoom(
        location = "Flooded Alcemy Room",
        description = "Vivid hues of moss and slime coat the walls, creating a surreal tapestry of colors. The floor,\nobscured by an unseen flood, bears witness to a chemical concoction that has transformed the\nenvironment into a mesmerizing yet mysterious spectacle. The amalgamation of diverse chemicals\nbeneath contributes to a uniquely vibrant and enigmatic atmosphere within these walls.",
        directions = {"south": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "Liqued Rune"),
    "magicalLibariy": CRoom(
        location = "Magical Libariy",
        description = "A whirlwind of books fills the air, with each tome rising from a pile on the ground,\nfloating gracefully to find its place on an infinite bookcase. Yet, the cycle repeats as\nthe books descend, creating a mesmerizing and perpetual dance of literature. The never-ending\nspectacle captures the essence of an unending cycle, where knowledge and stories take flight\nonly to return and continue their enchanting journey.",
        directions = {"north": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "Magic Rune"),
    "hiddenRituralSite": CRoom(
        location = "Hidden Ritural Site",
        description = "As you tread through the secretive ceremonial grounds, an unexpected revelation unfolds—the\nimposing Boss emerges from the shadows. This pivotal encounter marks a turning point,\npromising both challenges and profound revelations within the mysterious heart of this\nconcealed sanctuary.",
        directions = {"east": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "boss key")}
#border for UI
border = ("\n<------------------------------------------------------------------------------------------>\n")  
# Introduction
def introduction():
    clear()
    print(f"{border}\nIntroduction\n{border}")
    print("\nAmidst the mystical realm of Umaros, where tales of valor echo through the ages, you "
        "\nstand as a celebrated hero. The villagers sing songs of your past triumphs, and your "
        "\nname is synonymous with bravery and honor. However, a shadow looms over the "
        "\npeaceful village of Mentos, as the ancient giant Behemoth unleashes his wrath upon its "
        "\nunsuspecting dwellers."
        "\n"
        "\nThe once-thriving village now trembles in the face of Behemoth's malevolence, and a "
        "\ndesperate call for aid reaches your ears. As the hero of Umaros, duty calls you to "
        "\nembark on a perilous quest to rescue the besieged village and thwart the ancient "
        "\ngiant's rampage."
        "\n"
        "\nBehemoth's icy castle, a foreboding structure in the distant mountains, stands as the"
        "\nepicenter of the turmoil. To reach the heart of the storm and confront the colossal "
        "\nadversary, you must first unravel a cryptic riddle guarding the castle's entrance. Inside, "
        "\na critical artifact awaits the key to Behemoth's throne room, where the fate of Mentos "
        "\nhangs in the balance."
        "\n"
        "\nYour mission is clear: vanquish the ancient giant, restore peace to the village of "
        "\nMentos, and etch your name further into the annals of Umaros as a true hero. As you "
        "\nstand at the precipice of this epic journey, the time has come to choose your path. Will "
        "\nyou wield the arcane powers of a Mage, the unyielding strength of a Warrior, or the "
        "\ncunning finesse of a Rogue? The destiny of Umaros rests in your hands. Choose wisely "
        "\nand embark on your quest to secure victory and glory.\n")
    pressEnterToContinue()    
# Clears screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")
#Prompts the user to input to clear the screen
def pressEnterToContinue():
    input("press enter to continue ...")
    clear()
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
#Displays game over screen
def gameOver(playerCharacter):
    if playerCharacter.mHealth < 1:
        print(f"Score = {playerCharacter.mScore}")
        print("You lose Sucker!!!\n\nTry Again?\n\n")
        command = yeaOrNay("Yae/Nay: \n\n>")
        if command:
            menu()
        else:
            quitGame()
#Gets players name and makes sure its not too long or too short
def characterName():
    while True:
        clear()
        name = input(f"{border}\nTell me Hero, What is thy Name? (3 and 10 characters)\n{border}\n\n>").capitalize()
        if 3 <= len(name) <= 10:
            confirmName = yeaOrNay(f"{border} Is {name} your Name Yae/Nay: \n\n")
            if confirmName:
                return name
#Lets player choose what character to play as
def characterCreator():
        name = characterName()
        while True:
            clear()
            while True:
                command = input(f"{border}\n{name}, What type of hero are you?\n{border}\n1. warrior (easy)\n\n2. mage (medium)\n\n3. rogue (hard)\n\n>").lower()
                if command in ["warrior", "one", "1"]:
                    character = CCharacter(name, "Warrior", 200, [], 20, 0.30,["protection potion"], 0)
                    break
                elif command in ["mage", "two", "2"]:
                    character = CCharacter(name, "Mage", 150, [], 25,0.25, ["booster potion"], 0)
                    break
                elif command in ["rogue", "three", "3"]:
                    character = CCharacter(name, "Rogue", 130, [], 30, 0.20, ["damage potion"], 0)
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
#Random enemy generator
def randomEnemySelector(currentRoom):
    randomEnemy = random.randint(1,4)
    if currentRoom.mLocation == "Hidden Ritural Site":
        enemy = CCharacter("boss", None, 100, None, 30, 0.3, None, 500)
        return enemy
    elif randomEnemy == 1:
        enemy = CCharacter("Gobblin", None, 40, None, 12, 0.10, None, 100)
        return enemy
    elif randomEnemy == 2:
        enemy = CCharacter("Troll", None, 40, None, 18, 0.25, None, 130)
        return enemy
    elif randomEnemy == 3:
        enemy = CCharacter("Orc", None, 50, None, 16, 0.12, None, 150)
        return enemy
    elif randomEnemy == 4:
        enemy = CCharacter("Manticore", None, 70, None, 20, 0.28, None, 200)
        return enemy
#Random loot drops
def loot(playerCharacter):
    loot = ["health potion", "damage potion", "protection potion", "booster potion"]
    lootChance = random.randint(0,3)
    lootDropped = loot[lootChance]
    playerCharacter.addToInventory(lootDropped)
    return lootDropped
#Starting Main menu
def menu():
    while True:
        clear()
        print(f"{border}\n\t\t\tThe Hero of Umaros and the Giant Behemoth\n{border}\n"
              "\n1. New Game\n"
              "\n2. Load Game\n"
              "\n3. Help\n"
              f"\n4. Quit\n\n{border}")
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
#Allows the player to load a game save
def loadGame():
    clear()
    print("loagGame")
#Allows the player to exit the game
def quitGame():
    clear()
    print("Farewell, brave adventurer! Until we meet again.")
    return "quit"
#Allowas the player to recieve additional help
def help():
    clear()
    print(f"{border}\nHelp\n{border}\n\n"
          #general help
          "Type: help or h to open the instructions men\n\nType: quit or q to quit the game\n\nType: stats or s to show your charcters stats\n\nType: north, east, south or west for moving across rooms\n\nType the corrsponding number to what you would like to do\n"
          #combat help
          "\nType: attack, a or just pressing enter will allow you to attack\n\nrunning away will give the enemy a chance to to get a hit in")
    pressEnterToContinue()

def youWin(playerCharacter):
    clear()
    print(f"\n{border}\nCongratulations {playerCharacter.mName} You've WON!!!\n{border}\n Here is your over all Score {playerCharacter.mScore}\n\n would you like to play again?\n\n")
    pressEnterToContinue()
    command = yeaOrNay("Yae/Nay: \n\n>")
    if command:
        menu()
    else:
        quitGame()

def displayRoomInformation(currentRoom):
    clear()
    print(f"{border}"
          f"{currentRoom["location"]}"
          f"{border}"
          "\nCurrent Room Description:\n"
          f"\n{currentRoom["description"]}")
    print(border)

def combat(playerCharacter, currentRoom):
    command = ""
    enemy = randomEnemySelector(currentRoom)
    print(f"you see a {enemy.mName}\nYou have 3 options: ")
    while enemy.mHealth > 0 and playerCharacter.mHealth > 0:
        pressEnterToContinue()
        print(f"{playerCharacter.mName} {playerCharacter.mHealth} |  {enemy.mName}  {enemy.mHealth}")
        command = input(f"\na: attack\n\nr:Run away\n\nh: Help\n\nu: Use item>")
        if command in ["help", "h"]:
            help()
        if command in ["use item", "u"]:
            playerCharacter.useItem()
        if command in ["attack","a", ""]:
            print(f"You swing your weapon at {enemy.mName}")
            hitChance = random.randint(0,10)
            if hitChance > 3:
                clear()
                enemy.mHealth -= playerCharacter.mDamage
                print(f"succesful strike, enemy Health is now{enemy.mHealth}")
                if enemy.mHealth > 0:
                    playerCharacter.mHealth -= round(enemy.mDamage*playerCharacter.mDefence)
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
                playerCharacter.mHealth -= enemy.mDamage
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
                playerCharacter.mHealth -= enemy.mDamage
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
        riddle = CCharacter("Riddle 1 question", ["Riddle 1 anwser", "1"], None, None,"riddle 1 hint", None, None, 120)
        return riddle
    elif randomRiddle == 2:
        riddle = CCharacter("Riddle 2 question", ["Riddle 2 anwser", "2"], None, None,"riddle 2 hint", None, None, 120)
        return riddle
    elif randomRiddle == 3:
        riddle = CCharacter("Riddle 3 question", ["Riddle 3 anwser", "3"], None, None,"riddle 3 hint", None, None, 120)
        return riddle
    elif randomRiddle == 4:
        riddle = CCharacter("Riddle 4 question", ["Riddle 4 anwser", "4"], None, None,"riddle 4 hint", None, None, 120)
        return riddle

def riddle(playerCharacter):
    command = ""
    riddle = randomRiddleSelector()
    print (f"you hear an annoying voice, \nNEB: if you want the key riddle me this{riddle.mName}")
    while command != riddle.mHero:
        command = input("What is your anwser?\n\nh: help\n\nt: tip\n\nl: leave\n\n>").lower()
        if command in ["help", "h"]:
            help()
        if command in riddle.mHero:
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
    
# Modify the main function to loop based on the menu result
def main():
    while menu():  # Continue looping as long as the player wants to start a new game
        playerCharacter = characterCreator()
        introduction()
        currentRoom = rooms["enchantedForest"]
        while playerCharacter.mHealth >= 0:
            clear()
            currentRoom.displayLocationDescription()
            userInput = input(f"\nType one of the following commands:\n\nChange room: {currentRoom.mDirections}\n\nC: challenge\n\nS: Stats\n\nU: Use item\n\nH: Help\n\nE: Exit\n\n>").lower()
            if userInput in ["help", "h"]:
                help()
            elif userInput in ["challenge", "c"]:
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
                break  # Exit the game loop
        gameOver(playerCharacter)

if __name__ == "__main__":
    main()

    