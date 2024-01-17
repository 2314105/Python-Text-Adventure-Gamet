#Import librarys
import os
import random
import time
#Character class
class CCharacter:
    def __init__(self, name, hero, health, magic, damage, defence, inventory):
        self.mName = name
        self.mHero = hero
        self.mHealth = health
        self.mMagic = magic
        self.mDamage = damage
        self.mDefence = defence
        self.mInventory = inventory
    #Displays players stats
    def playerStats(self):
        clear()
        print(f"{border}\nName: {self.mName}\n{border}"
              f"\nClass: {self.mHero}"
              f"\nHP: {self.mHealth}"
              f"\nMP: {self.mMagic}"
              f"\nAttack: {self.mDamage}"
              f"\nDeffence: {self.mDefence}\n{border}"
              f"\nInventory : {self.mInventory}\n{border}")
    #Adds items to inventory
    def addToInventory(self, item):
        self.mInventory.append(item)
        print(f"{item} added to inventory.")
    #Uses item from inventory, adds it to stats and removes it from list
    def useItem(self):
        clear()
        command = input(f"\n{border}\nWhat item would you like to use\n{border}\nInventory: {self.mInventory}\n{border}\n>").lower()
        if command in self.mInventory:
            if command == "health potion":
                self.mHealth += 30
                self.mInventory.remove("health potion")
                print("Your health has increased by 30 points")
            elif command == "magic damage potion":
                self.mMagic += 12
                self.mInventory.remove("magic damage potion")
                print("Your magic damage has increased by 12 points")
            elif command == "physical damage potion":
                self.mDamage += 14
                self.mInventory.remove("physical damage potion")
                print("Your physical damage has increased by 14 points")
            elif command == "defence potion":
                self.mDefence += 10
                self.mInventory.remove("defence potion")
                print("Your Defence has increased by 10 points")
            elif command == "booster potion":
                self.mMagic += 5
                self.mDefence += 5
                self.mDamage += 5
                self.mHealth += 5
                self.mInventory.remove("booster potion")
                print(f"All Your stats have increased by 5")
            else:
                print(f"{command} not recognised.")
                pressEnterToContinue()
        else:
            print(f"{command} is not in your inventory")
            pressEnterToContinue()

    #Displays enemys stats
    def enemyStats(self):
        print(f"\nName: {self.mName}"
              f"\nHP: {self.mHealth}"
              f"\nAttack: {self.mDamage}"
              f"\nDeffence: {self.mDefence}")    
# rooms class
class CRoom:
    def __init__(self, location, description, directions, challenge, item):
        self.mLocation = location
        self.mDescription = description
        self.mDirections = directions
        self.mChallenge = challenge
        self.mItem = item

    def displayLocationDescription(self):
        print(f"\n{border}\nLocation: {self.mLocation}\n{border}\n{self.mDescription}\n{border}")

    def navigation(self, direction):
        if self.mChallenge and not self.mChallenge["completed"]:
            print("You must complete the challange before moving to the next room")
            pressEnterToContinue()
            return self
        elif direction in self.mDirections:
            nextRoom = self.mDirections[direction]
            return rooms[nextRoom]
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
        item = ["Enchanted Rune"]),
    "frozenStoneGarden": CRoom(
        location = "Frozen Stone Garden",
        description = "In this frigid landscape, an intense cold envelops everything. Frozen statues dot the\nsurroundings, revealing upon closer examination that they are not sculptures but the chilling\nfate of people and creatures caught in an icy stasis. The profound stillness of this frozen\nrealm conceals the silent stories of those who succumbed to the relentless grip of cold.",
        directions = {"north": "floodedAlcemyRoom", "east": "enchantedForest", "south": "magicalLibariy", "west": "hiddenRituralSite"},
        challenge = {"completed": False},
        item = ["Ice Rune"]),
    "floodedAlcemyRoom": CRoom(
        location = "Flooded Alcemy Room",
        description = "Vivid hues of moss and slime coat the walls, creating a surreal tapestry of colors. The floor,\nobscured by an unseen flood, bears witness to a chemical concoction that has transformed the\nenvironment into a mesmerizing yet mysterious spectacle. The amalgamation of diverse chemicals\nbeneath contributes to a uniquely vibrant and enigmatic atmosphere within these walls.",
        directions = {"south": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = ["Liqued Rune"]),
    "magicalLibariy": CRoom(
        location = "Magical Libariy",
        description = "A whirlwind of books fills the air, with each tome rising from a pile on the ground,\nfloating gracefully to find its place on an infinite bookcase. Yet, the cycle repeats as\nthe books descend, creating a mesmerizing and perpetual dance of literature. The never-ending\nspectacle captures the essence of an unending cycle, where knowledge and stories take flight\nonly to return and continue their enchanting journey.",
        directions = {"north": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = ["Magic Rune"]),
    "hiddenRituralSite": CRoom(
        location = "Hidden Ritural Site",
        description = "As you tread through the secretive ceremonial grounds, an unexpected revelation unfolds—the\nimposing Boss emerges from the shadows. This pivotal encounter marks a turning point,\npromising both challenges and profound revelations within the mysterious heart of this\nconcealed sanctuary.",
        directions = {"east": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = ["Green Rune"])}
#border for UI
border = ("\n<------------------------------------------------------------------------------------------>\n")      
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
def gameOver(playerCharacter, score):
    if playerCharacter.mHealth < 1:
        print(f"Score = {score}")
        print("You lose Sucker!!!")
#Gets players name and makes sure its not too long or too short
def characterName():
    while True:
        clear()
        name = input(f"{border}\nTell me Hero, What is thy Name?\n{border}\n\n>").capitalize()
        if 3 <= len(name) <= 10:
            confirm_name = yeaOrNay(f"{border} Is {name} your Name Yae/Nay: \n\n")
            if confirm_name:
                return name
        else:
            print("\nInvalid name length. Your name should be between 4 and 10 characters.")
            input(f"{border}Press enter to try again{border}\n>")
#Lets player choose what character to play as
def characterCreator():
        name = characterName()
        while True:
            clear()
            while True:
                command = input(f"{border}\n{name}, What type of hero are you?\n{border}\n1. warrior\n\n2. mage\n\n3. rogue").lower()
                if command in ["warrior", "one", "1"]:
                    character = CCharacter(name, "Warrior", 100, 6, 18, 6,["defence potion"])
                    break
                elif command in ["mage", "two", "2"]:
                    character = CCharacter(name, "Mage", 80, 18, 7, 4, ["magic potion"])
                    break
                elif command in ["rogue", "three", "3"]:
                    character = CCharacter(name, "Rogue", 60, 20, 20, 2, ["damage potion"])
                    break
            character.playerStats()
            command = yeaOrNay("Is this your class Yae/Nay: \n\n>")
            if command:
                return character
#Random enemy generator
def randomEnemySelector():
    randomEnemy = random.randint(1,4)
    if randomEnemy == 1:
        enemy = CCharacter("Gobblin", None, 20, 100, 12, 10, None)
        return enemy
    elif randomEnemy == 2:
        enemy = CCharacter("Troll", None, 30, 120, 18, 20, None)
        return enemy
    elif randomEnemy == 3:
        enemy = CCharacter("Orc", None, 40, 140, 16, 10, None)
        return enemy
    elif randomEnemy == 4:
        enemy = CCharacter("Manticore", None, 50, 200, 28, 28, None)
        return enemy
#Random loot drops
def loot(playerCharacter):
    loot = ["health potion", "physical damage potion", "defence potion", "magic damage potion", "booster potion"]
    lootChance = random.randint(0,2)
    lootDropped = loot[lootChance]
    playerCharacter.addToInventory(lootDropped)
    return lootDropped
# Uses the enemy magic or riddle magic as score
def score(enemy, riddle, currentScore):
    if enemy:
        updatedScore = currentScore + enemy.mMagic
    elif riddle:
        updatedScore = currentScore + riddle.mMagic
    else:
        updatedScore = currentScore
    return updatedScore
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
            break
        elif command == "2" or command == "load game" or command == "two":
            loadGame()
            break
        elif command == "3" or command == "help" or command == "three" or command == "h":
            help()
        elif command == "4" or command == "quit" or command == "four" or command == "q":
            quitGame()
            break 
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

def displayRoomInformation(currentRoom):
    clear()
    print(f"{border}"
          f"{currentRoom["location"]}"
          f"{border}"
          "\nCurrent Room Description:\n"
          f"\n{currentRoom["description"]}")
    print(border)

def combat(playerCharacter, currentScore):
    command = ""
    enemy = randomEnemySelector()
    print(f"you see a {enemy.mName}\nYou have 3 options: ")
    while enemy.mHealth > 0 and playerCharacter.mHealth > 0:
        pressEnterToContinue()
        print(f"{playerCharacter.mName} {playerCharacter.mHealth} |  {enemy.mName}  {enemy.mHealth}")
        command = input(f"\n1.Physical attack\n\n2.Magic attack\n\n3.Run away")
        #physical damage change to a function
        if command in ["physical attack", "one", "1"]:
            print(f"You swing your weapon at {enemy.mName}")
            hitChance = random.randint(0,10)
            if hitChance > 4:
                enemy.mHealth -= playerCharacter.mDamage
                print(f"succesful strike, enemy Health is now{enemy.mHealth}")
                if enemy.mHealth > 0:
                    playerCharacter.mHealth -= enemy.mDamage-playerCharacter.mDefence
                    print(f"{enemy.mName} takes a hits you, you now have {playerCharacter.mHealth}")
                    gameOver(playerCharacter, currentScore)
                else:
                    lootDropped = loot(playerCharacter)
                    currentScore = score(enemy, None, currentScore)
                    print(f"you have defeated the {enemy.mName}, it looks like it dropped somthing \nLoot: {lootDropped}\nScore: {currentScore}")
                    pressEnterToContinue()
                    break
            else:
                print(f"your miss the {enemy.mName} leaving a opening for a counter attack")
                playerCharacter.mHealth -= enemy.mDamage
                print(f"{enemy.mName} landed a full damage hit,ignoring your deffence; current health is {playerCharacter.mHealth}")
                gameOver(playerCharacter, currentScore)
        #magic damage change to a function
        elif command in ["magic attack", "two", "2"]:
            print(f"You cast your spell at {enemy.mName}")
            hitChance = random.randint(0,10)
            if hitChance > 4:
                enemy.mHealth -= playerCharacter.mMagic
                print(f"succesful strike, enemy Health is now{enemy.mHealth}")
                if enemy.mHealth > 0:
                    playerCharacter.mHealth -= (enemy.mDamage-playerCharacter.mDefence)
                    print(f"{enemy.mName} takes a hits you, you now have {playerCharacter.mHealth}")
                    gameOver(playerCharacter, currentScore)
                else:
                    lootDropped = loot(playerCharacter)
                    currentScore = score(enemy,None, currentScore)
                    print(f"you have defeated the {enemy.mName}, it looks like it dropped somthing \nLoot: {lootDropped}\nScore: {currentScore}")
                    pressEnterToContinue()

                    break
            else:
                print(f"your miss the {enemy.mName} leaving a opening for a counter attack")
                playerCharacter.mHealth -= enemy.mDamage
                print(f"{enemy.mName} landed a full damage hit,ignoring your deffence; current health is {playerCharacter.mHealth}")
                gameOver(playerCharacter, currentScore)
        #escape change to a function?
        elif command in ["run away", "three", "3"]:
            print("You try running away")
            hitChance = random.randint(0, 10)
            if hitChance > 3:
                print("You managed to escape")
                break
            else:
                print(f"You tried to escape but the {enemy.mName} was able to get you, Your Health {playerCharacter.mHealth}")
                playerCharacter.mHealth -= enemy.mDamage
                gameOver(playerCharacter, currentScore)
                
        else:
            print(f"{command} not recognised")

def challenge(currentRoom, playerCharacter, currentScore,):
    if currentRoom.mChallenge and not currentRoom.mChallenge["completed"]:
        print(f"A challenge in {currentRoom.mLocation} awaits you.")
        challengeType = random.choice(["riddle", "combat"])
        clear()
        if challengeType == "riddle": 
            riddle(playerCharacter, currentScore)
        elif challengeType == "combat":
            combat(playerCharacter, currentScore)
        playerCharacter.addToInventory(currentRoom.mItem)
        currentRoom.mChallenge["completed"] = True
    else:
        print(f"The challenge in {currentRoom.mLocation} has already been completed.")

def randomRiddleSelector():
    randomRiddle = random.randint(1,4)
    if randomRiddle == 1:
        riddle = CCharacter("Riddle 1 question", ["Riddle 1 anwser", "1"], None, 120,"riddle 1 hint", None, None)
        return riddle
    elif randomRiddle == 2:
        riddle = CCharacter("Riddle 2 question", ["Riddle 2 anwser", "2"], None, 130,"riddle 2 hint", None, None)
        return riddle
    elif randomRiddle == 3:
        riddle = CCharacter("Riddle 3 question", ["Riddle 3 anwser", "3"], None, 140,"riddle 3 hint", None, None)
        return riddle
    elif randomRiddle == 4:
        riddle = CCharacter("Riddle 4 question", ["Riddle 4 anwser", "4"], None, 200,"riddle 4 hint", None, None)
        return riddle

def riddle(playerCharacter, currentScore):
    command = ""
    riddle = randomRiddleSelector()
    print (f"you hear an annoying voice, \nNEB: if you want the key riddle me this{riddle.mName}")
    while command != riddle.mHero:
        pressEnterToContinue()
        command = input("What is your anwser?")
        if command in riddle.mHero:
            currentScore = score(None, riddle, currentScore)
            print(f"Well done {playerCharacter.mName} you guessed correctly")
            break

        elif command == "help".lower():
            print(f"ahh struggling are we, here this should help: \n\n>{riddle.mDamage}")
            pressEnterToContinue()

        elif command == "leave".lower():
            break
        else:
            print(f"{command} not recognised")

def introduction():
    clear()
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
        "\nand embark on your quest to secure victory and glory.")
    pressEnterToContinue()
    
def main():
    currentScore = 0
    menu()
    playerCharacter = characterCreator()
    currentRoom = rooms["enchantedForest"]
    while True:
        clear()
        currentRoom.displayLocationDescription()
        userInput = input(f"\nEnter one of the following commands:\n\nChallenge: challenge\n\nChange room: {currentRoom.mDirections}\n\nHelp: help\n\nExit: exit\n\n>").lower()
        if userInput == "help":
            help()
        elif userInput == "challenge":
            challenge(currentRoom, playerCharacter, currentScore)
        elif userInput == "stats":
            playerCharacter.playerStats()
        elif userInput == "use item":
            playerCharacter.useItem()
        elif userInput == 'exit':
            menu()
            break

        currentRoom = currentRoom.navigation(userInput)
if __name__ == "__main__":
    main()

    