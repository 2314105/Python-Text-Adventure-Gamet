#Import librarys
import os
import random
import time

#Character class
class CCharacter:
    def __init__(self, name, hero, health, magic, damage, defence):
        self.mName = name
        self.mHero = hero
        self.mHealth = health
        self.mMagic = magic
        self.mDamage = damage
        self.mDefence = defence
    #Displays players stats
    def playerStats(self):
        print(f"\nName: {self.mName}"
              f"\nClass: {self.mHero}"
              f"\nHP: {self.mHealth}"
              f"\nMP: {self.mMagic}"
              f"\nAttack: {self.mDamage}"
              f"\nDeffence: {self.mDefence}")
    #Displays enemys stats
    def enemyStats(self):
        print(f"\nName: {self.mName}"
              f"\nHP: {self.mHealth}"
              f"\nAttack: {self.mDamage}"
              f"\nDeffence: {self.mDefence}")
        
#rooms class
class CRoom:
    def __init__(self, location, description, direction, challange, item, hint):
        self.mLocation = location
        self.mDescription = description
        self.mDirection = direction
        self.mChallange = challange
        self.mItem = item
        self.mHint = hint

    def displayLocationDescription(self):
        print(f"\nLocation: {self.mLocation}\n{self.mDescription}")

    rooms = {
    "enchantedForest": {
        "location": "Enchanted Forest",
        "description": "Surrounded by tall, dark trees, you stand in a mystical forest. Blue leaves gently descend"
        "\nfrom the sky, casting an ethereal glow upon the surroundings. The air is filled with"
        "\nenchantment as the magical foliage paints the scene with its serene illumination.",
        "west": "frozenStoneGarden",
        "item": ["Blue Rune"],
        "challenge":{
            "completed": False}},
    "frozenStoneGarden": {
        "location": "Frozen Stone Garden",
        "description": "In this frigid landscape, an intense cold envelops everything. Frozen statues dot the"
        "\nsurroundings, revealing upon closer examination that they are not sculptures but the chilling"
        "\nfate of people and creatures caught in an icy stasis. The profound stillness of this frozen"
        "\nrealm conceals the silent stories of those who succumbed to the relentless grip of cold.",
        "north": "floodedAlcemyRoom",
        "east": "enchantedForest",
        "south": "magicalLibariy",
        "west": "hiddenRituralSite",
        "item": ["Red Rune"],
        "challenge":{
            "completed": False    }},
    "floodedAlcemyRoom": {
        "location": "Flooded Alcemy Room",
        "description": "Vivid hues of moss and slime coat the walls, creating a surreal tapestry of colors. The floor,"
        "\nobscured by an unseen flood, bears witness to a chemical concoction that has transformed the"
        "\nenvironment into a mesmerizing yet mysterious spectacle. The amalgamation of diverse chemicals"
        "\nbeneath contributes to a uniquely vibrant and enigmatic atmosphere within these walls.",
        "south": "frozenStoneGarden",
        "item": ["Green Rune"],
        "challenge":{
            "completed": False}},
    "magicalLibariy": {
        "location": "Magical Libariy",
        "description": "A whirlwind of books fills the air, with each tome rising from a pile on the ground,"
        "\nfloating gracefully to find its place on an infinite bookcase. Yet, the cycle repeats as"
        "\nthe books descend, creating a mesmerizing and perpetual dance of literature. The never-ending"
        "\nspectacle captures the essence of an unending cycle, where knowledge and stories take flight"
        "\nonly to return and continue their enchanting journey.",
        "north": "frozenStoneGarden",
        "item": ["Yellow rune"],
        "challenge":{
            "completed": False}},
    "hiddenRituralSite": {
        "location": "Hidden Ritural Site",
        "description": "As you tread through the secretive ceremonial grounds, an unexpected revelation unfolds—the"
        "\nimposing Boss emerges from the shadows. This pivotal encounter marks a turning point,"
        "\npromising both challenges and profound revelations within the mysterious heart of this"
        "\nconcealed sanctuary.",
        "east": "frozenStoneGarden",
        "item": [],
        "challenge":{
            "completed": False}}}

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
    clear()
    while True:
        name = input("Tell me Hero, What is thy Name\n\n>").capitalize()
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
                command = input(f"{name}, What type of hero are you?\n1. warrior\n\n2. mage\n\n3. rogue").lower()
                if command in ["warrior", "one", "1"]:
                    character = CCharacter(name, "Warrior", 100, 6, 18, 6)
                    break
                elif command in ["mage", "two", "2"]:
                    character = CCharacter(name, "Mage", 80, 18, 7, 4)
                    break
                elif command in ["rogue", "three", "3"]:
                    character = CCharacter(name, "Rogue", 60, 20, 20, 2)
                    break

            character.playerStats()
            command = yeaOrNay(f"{border} Is this your class Yae/Nay: \n\n")
            if command:
                return character
#Random enemy generator
def randomEnemySelector():
    randomEnemy = random.randint(1,4)
    if randomEnemy == 1:
        enemy = CCharacter("Gobblin", None, 20, 100, 12, 10)
        return enemy
    elif randomEnemy == 2:
        enemy = CCharacter("Troll", None, 30, 120, 18, 20)
        return enemy
    elif randomEnemy == 3:
        enemy = CCharacter("Orc", None, 40, 140, 16, 10)
        return enemy
    elif randomEnemy == 4:
        enemy = CCharacter("Manticore", None, 50, 200, 28, 28)
        return enemy
#Random loot drops
def loot():
    loot = ["Health potion", "Damage Potion", "Defence potion"]
    lootChance = random.randint(0,2)
    lootDropped = loot[lootChance]
    return lootDropped
#Uses the enemy magic as score
def score(enemy, riddle, currentScore):
    updatedScore =currentScore + enemy.mMagic or riddle.mMagic
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
                    lootDropped = loot()
                    currentScore = score(enemy, currentScore)
                    print(f"you have defeated the {enemy.mName}, it looks like it dropped somthing \nLoot: {lootDropped}\nScore: {currentScore}")
                    break
            else:
                print(f"your miss the {enemy.mName} leaving a opening for a counter attack")
                playerCharacter.mHealth - enemy.mDamage
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
                    lootDropped = loot()
                    currentScore = score(enemy, currentScore)
                    print(f"you have defeated the {enemy.mName}, it looks like it dropped somthing \nLoot: {lootDropped}\nScore: {currentScore}")
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

def challenge(currentRoom, playerCharacter, currentScore):
    if "challenge" in currentRoom and not currentRoom["challenge"]["completed"]:
        challengeType = random.choice(["riddle", "combat"])
        clear()
        if challengeType == "riddle": 
            riddle(playerCharacter, currentScore)
        elif challengeType == "combat":
            combat(playerCharacter, currentScore)
        currentRoom["challenge"]["completed"] = True


def randomRiddleSelector():
    randomRiddle = random.randint(1,4)
    if randomRiddle == 1:
        riddle = CCharacter("Riddle 1 question", ["Riddle 1 anwser", "1"], None, 120,"riddle 1 hint", None)
        return riddle
    elif randomRiddle == 2:
        riddle = CCharacter("Riddle 2 question", ["Riddle 2 anwser", "2"], None, 130,"riddle 2 hint", None)
        return riddle
    elif randomRiddle == 3:
        riddle = CCharacter("Riddle 3 question", ["Riddle 3 anwser", "3"], None, 140,"riddle 3 hint", None)
        return riddle
    elif randomRiddle == 4:
        riddle = CCharacter("Riddle 4 question", ["Riddle 4 anwser", "4"], None, 200,"riddle 4 hint", None)
        return riddle

def riddle(playerCharacter, currentScore):
    command = ""
    riddle = randomRiddleSelector()
    print (f"you hear an annoying voice, \nNEB: if you want the key riddle me this{riddle.mName}")
    while command != riddle.mHero:
        pressEnterToContinue()
        command = input("What is your anwser?")
        if command in riddle.mHero:
            currentScore = score(riddle, currentScore)
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
    
def main(currentRoom, currentScore):
    directions =["north", "south", "east", "west"]
    currentRoom = rooms["enchantedForest"]
    menu()
    playerCharacter = characterCreator()
    introduction()
# game loop
    while True:
        displayRoomInformation(currentRoom)
        command = input('\nWhat do you do?').lower()
        # movement
        if command in directions:
            if command in currentRoom:
                nextRoom = currentRoom[command]
                currentRoom = rooms[nextRoom]
                challenge(playerCharacter, currentScore, currentRoom)
            else:
                print("You can't move in that direction.")
                pressEnterToContinue()
        #Help
        elif command == "h" or command == "help":
            help()
        
        # quit game
        elif command == "q" or command == "quit":
            menu()
            break
        
        elif command == "s" or command == "stats":
            playerCharacter.playerStats()
            pressEnterToContinue()
        
        # gather objects
        
        else:
            print("I don't understand that command.")
if __name__ == "__main__":
    main("enchantedForest", 0)
    
