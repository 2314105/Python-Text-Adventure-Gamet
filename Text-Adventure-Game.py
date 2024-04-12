# Import librarys
import os
import random
import time

# Character class
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

    # Displays players stats
    def PlayerStats(self):
        Clear()
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
        
    # Adds items to inventory
    def AddToInventory(self, item):
        self.mInventory.append(item)
        print(f"{item} added to inventory.")

    # Uses item from inventory, adds it to stats, and removes it from list
    def UseItem(self):
        
        # Initialize potion effects
        healthEffect = 30
        damageEffect = 15
        defenceEffect = 0.1
        boosterHealthEffect = 5
        boosterDamageEffect = 5
        boosterDefenceEffect = 0.05
        Clear()
        
        # Prompt the player to choose an item from their inventory
        userInput = input(f"\n{border}\nWhat item would you like to use\n{border}\nInventory: {self.mInventory}\n{border}\n>").lower()
        if userInput in ["health", "health potion", "h"]:
            
            # Check if the player has a health potion in their inventory apply health effect, remove the item from inventory, and inform the player
            if "health potion" in self.mInventory:
                self.mHealth += healthEffect
                self.mInventory.remove("health potion")
                print("Your health has increased by 30 points")
        elif userInput in ["damage", "damage potion", "d"]:
            if "damage potion" in self.mInventory:
                self.mDamage += damageEffect
                self.mInventory.remove("damage potion")
                print("Your physical damage has increased by 15 points")
        elif userInput in ["protection", "protection potion", "p"]:
            if "protection potion" in self.mInventory:
                self.mDefence += defenceEffect
                self.mInventory.remove("protection potion")
                print("Your protection has increased by 0.1%")
        elif userInput in ["boost","booster", "booster potion", "b"]:
            if "booster potion" in self.mInventory:
                self.mDefence += boosterDefenceEffect
                self.mDamage += boosterDamageEffect
                self.mHealth += boosterHealthEffect
                self.mInventory.remove("booster potion")
                print("All your stats have increased by 5 and defence by 0.05%")
        else:
            # Inform the player of unrecognized input
            print(f"{userInput} not recognized.")
            PressEnterToContinue()

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
        
    # Calls Askii art from text file and displays art based on the lines from the constructors
    def AskiiArt(self):
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[self.mFirstLine-1:self.mLastLine-1]:
                print(line.rstrip())

    # Displays the current rooms description
    def DisplayLocationDescription(self):
        self.AskiiArt()
        print(f"\n{border}\nLocation: {self.mLocation}\n{border}\n{self.mDescription}\n{border}")
        # Check if the challenge in the room has been completed
        if "completed" in self.mChallenge and self.mChallenge["completed"]:
            print(f"Challenge completed{border}")
        else:
            print(f"Challenge not completed{border}")

    # Navigate rooms
    def Navigation(self, direction, playerCharacter):
    # Checks if the rooms challenge has been completed
        if self.mChallenge and not self.mChallenge["completed"]:
            print("NEB: You've got to complete my challenge before moving on.")
            PressEnterToContinue()
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
                    PressEnterToContinue()
                    return self
            else:
                return nextRoom
        else:
            PressEnterToContinue()
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
        description = "As you tread through the secretive ceremonial grounds, an unexpected revelation unfolds—the"
        "\nimposing Boss emerges from the shadows. This pivotal encounter marks a turning point,"
        "\npromising both challenges and profound revelations within the mysterious heart of this"
        "\nconcealed sanctuary.",
        directions = {"east": "frozenStoneGarden"},
        challenge = {"completed": False},
        item = "boss key",
        firstLine = 324,
        lastLine = 355)}

# Border for UI
border = ("\n<==========================================================================================>\n")  

# Introduction
def Introduction(playerCharacter):
    Clear()
    print(f"{border}Introduction{border}")
    print(f"Greetings {playerCharacter.mName}, you are the hero sent from the kingdom Umaros tasked with saving the"
        "\nvillage of Mentos. They are currently under tyrnical rule of a giant known mostly as behmoth"
        "\nit's also been rumed that he now has a dragon under his userInput so please be carfule in"
        "\nyour future conquest. The icy castle is full of traps and riddles, any time an adventurer"
        "\nhas gone there they've never returned, this could be the ghost of a ghostly gnome known as"
        "\nNEB. It's known that Neb likes to close the gates behind people entrapping them in rooms"
        "\nuntill the challenge has been complete, so stay vigilant and be aware of your surroundings")
    PressEnterToContinue()    
    print(f"{border}Introduction{border}")
    print("Each room has a challenge to progress to the next, the room challange must be completed to"
          "\ngain the key forfeiting the challange will complete the room but you will gain no score"
          "\nand in combat situationsyou may risk getting attacked and not escaping."
          "\n\nAll four runes need to be collected to enter the boss room, these are collected by\n"
          "\ncompleteing room challanges"
          "\nChallanges are randomly generated between combat and a riddle, and from there the"
          "\nriddle or combat is also randomly chosen, making a sure that not all games are the same.")
    PressEnterToContinue()

# Clears screen
def Clear():
    os.system('cls')

# Prompts the user to input to clear the screen
def PressEnterToContinue():
    input("press enter to continue ...")
    Clear()

# Yes or no question to return eigther True or False
def YeaOrNay(prompt):
    while True:
        userInput = input(prompt).lower()
        if userInput in ["yes", "y", "yea"]:
            return True
        elif userInput in ["no", "n", "nay"]:
            return False
        else:
            print("Invalid input. Please enter Yea or Nay.")

# Displays game over screen depending on the players health or if the behemoth has been defeated
def GameOver(playerCharacter, behemothDefeated, startTimer):
    if playerCharacter.mHealth < 1:
        PressEnterToContinue()
        print(border)
        
        # Opens a file containing ASCII art and prints game over
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[201:208]:
                print(line.rstrip())
        print(f"{border}Score = {playerCharacter.mScore}{border}")
        print("\nTry Again?\n\n")
        userInput = YeaOrNay("Yae/Nay: \n\n>")
        if userInput:
            return False
        else:
            QuitGame()
            return True
    elif behemothDefeated == True:
        return YouWin(playerCharacter, startTimer)
        
# Gets players name and makes sure its not too long or too short and capitalizes it
def CharacterName():
    while True:
        Clear()
        name = input(f"{border}\nTell me Hero, What is thy Name? (3 and 10 characters)\n{border}\n\n>").capitalize()
        if 3 <= len(name) <= 10:
            confirmName = YeaOrNay(f"{border} Is {name} your Name Yae/Nay: \n\n")
            if confirmName:
                return name
            
# Lets player choose what character to play as
def CharacterCreator():
        # Gets name of the user
        name = CharacterName()
        while True:
            Clear()
            # Loops until the user has selected a hero
            while True:
                # Prompts the user to select a character type
                userInput = input(f"{border}\n{name}, What type of hero are you?\n{border}\n1. warrior (easy)\n\n2. mage (medium)\n\n3. rogue (hard)\n\n>").lower()
                if userInput in ["warrior", "one", "1"]:
                    character = CCharacter(name, "Warrior", 300, [], 40, 0.30,["protection potion"], 0, 97, 123)
                    break
                elif userInput in ["mage", "two", "2"]:
                    character = CCharacter(name, "Mage", 200, [], 50,0.25, ["booster potion"], 0, 76, 97)
                    break
                elif userInput in ["rogue", "three", "3"]:
                    character = CCharacter(name, "Rogue", 170, [], 70, 0.20, ["damage potion"], 0, 123, 143)
                    break
                else:
                    print(f"{name}, {userInput} is not one of the options, please try again")
                    PressEnterToContinue()
            # Displays the players stats and information
            character.PlayerStats()
            if character.mHero == "Warrior":
                 print("The Warrior is the easiest of the three classes, with a high health pool, high \nphysical damage and a strong defence makes then ideal for your first play through.\n")
            elif character.mHero == "Mage":
                print("The Mage is a medium diffculty class, if you're looking for a bit of a challenge and \nwant to weild the arcane arts pick mage.\n")
            else:
                print("The Rogue class is the hardest out of all three, if youre feeling lucky you can get \nsome series damage out, but ifyour hit its gunna hurt.\n")
                
            userInput = YeaOrNay("Is this your class Yae/Nay: \n\n>")
            if userInput:
                return character
            
# Main menu to help navigate the start of the game
def Menu():
    # Infinite loop to continuously display the menu until a valid choice is made
    while True:
        Clear()
        
        # Prints ASCII art
        with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[0:29]:
                print(line.rstrip())
                
        # Prints the main menu options
        print(f"{border}\n\t\t\tThe Hero of Umaros and the Giant Behemoth\n{border}"
              "1. Start Game\n"
              "2. Leader Board\n"
              "3. Help\n"
              f"4. Quit{border}")
        # Prompts the player to enter their choice
        userInput = input("Type thy choice:\n\n> ").lower()
        # Checks the player's input and performs corresponding actions
        if userInput in ["1", "one", "start game", "start"]:
            # Create the player character
            playerCharacter = CharacterCreator()
            currentRoom = rooms["enchantedForest"]
            Introduction(playerCharacter)
            return playerCharacter , currentRoom
        elif userInput in ["2", "two", "leader board"]:
            # Displays the leaderboard by reading scores from a file
            DisplayLeaderBoard()
        elif userInput in["3", "three", "help"]:
            # Displays the help menu
            Help()
        elif userInput in ["4", "four", "quit"]:
            # Quits the game
            QuitGame()
            # Returns False to indicate not starting a new game
            return False

# Allows the player to exit the game
def QuitGame():
    Clear()
    print("Farewell, brave adventurer! Until we meet again.")

# Allows the player to recieve additional help
def Help():
    Clear()
    print(f"{border}\nHelp\n{border}\n"
    "General:\n-Type: help or h to open the instructions menu\n-Type: quit or q to quit the game\n-Type: use item or u to check your inventory and use an item-\n-Type: stats or s to show your charcters stats\n-Type: north, east, south or west for moving across rooms"
    "\n\nCombat:\n-Type: attack, a or just pressing enter will allow you to attack quickly\n-Running away will give the enemy a chance to to get a hit in\n-Type: U or use item to use oneof te potion in your invenory"
    "\n\nRiddle:\n-Type: tip or t will give you a hint for the riddle"
    "\n\nBoth challange situations you can forfeit, but you wont gain any score."
    "\n\nPotions:\n-Potions can be used by using the 'use item' function, from there type the\n potion out or type the first letter. E.G:\nh => health potion\nd => damage potion\np => protection potion\nb => booster potion\n")
    PressEnterToContinue()

# Save score to txt file
def SaveScore(playerCharacter, startTimer):
    endTimer = time.time()
    timeScore = round(endTimer-startTimer,2)
    with open("Score.txt", "a") as file:
        file.write(f"{playerCharacter.mName},{playerCharacter.mScore},{timeScore}\n")

# Displays the top 10 scores from the Score.txt file
def DisplayLeaderBoard():
    # Initialize arrays to store the scores
    nameAndScore = []
    timeScore = []
    groupedScore = {}
    counter = 0
    
    # Open file and read all lines
    with open("Score.txt", "r") as file:
        lines = file.readlines()
        
        # Loop through each line and split the data
        for line in lines:
            data = line.strip().split(",")
            name = data[0]
            time = float(data[2])
            nameAndScore.append((name, time))
            timeScore.append(time)
            groupedScore[time] = [name, data[1]]

        # Sorting time score using bubble sort
        n = len(timeScore)
        for i in range(n):
            for j in range(0, n-i-1):
                if timeScore[j] > timeScore[j+1]:
                    timeScore[j], timeScore[j+1] = timeScore[j+1], timeScore[j]

        # Display the top 10 scores
        Clear()
        print(f"{border}\t\t\t\t\tTop 10 Scores:{border}")
        for i in range(min(10, len(nameAndScore))):
            counter += 1
            time = timeScore[i]
            name, level = groupedScore[time]
            print(f"\t\t\t{counter}. Name: {name}, Time: {time}, Level: {level}\n")  
        print(border)  
        PressEnterToContinue()

# You win Screen with ASCII art and saving score
def YouWin(playerCharacter, startTimer):
    Clear()
    print(border)
    SaveScore(playerCharacter, startTimer)
    # Opens a file containing ASCII art and prints victory
    with open('AskiiArt.txt', 'r') as artFile:
            for line in artFile.readlines()[208:215]:
                print(line.rstrip())
    PressEnterToContinue()
    Menu()
    return False

# Calls current room and displays information with UI
def DisplayRoomInformation(currentRoom):
    Clear()
    print(f"{border}"
          f"{currentRoom["location"]}"
          f"{border}"
          "\nCurrent Room Description:\n"
          f"\n{currentRoom["description"]}")
    print(border)

# Player vs Enemy combat
def Combat(playerCharacter, currentRoom):
    # Initialize userInput input variable
    userInput = ""
    # Select a random enemy for the current room
    enemy = RandomEnemySelector(currentRoom)
    # Display enemy information
    print(f"As you look around the {currentRoom.mLocation}, you hear a ghostly voice, its"
          f"\nNEB the ghostly gnome. NEB: hey there's a {enemy.mName} over there, if you defeate it"
          "\nyou'll get some good loot that might help with the final boss, if not i'll let you"
          f"\nout, make sure to grab that key though.\n{border}")
    # Main combat loop
    while enemy.mHealth > 0 and playerCharacter.mHealth > 0:
        # Generate random damage for each turn
        randomDamage = random.randint(0, 5)
        PressEnterToContinue()
        # Display enemy ASCII art and health information
        enemy.AskiiArt()
        print (border)
        print(f"{playerCharacter.mName} {playerCharacter.mHealth} |  {enemy.mName}  {enemy.mHealth}{border}")
        userInput = input(f"a: Attack\nr: Run away\nh: Help\nu: Use item\n\n>").lower()
        # Handle different player userInputs
        if userInput in ["help", "h"]:
            Help()
        elif userInput in ["use item", "u"]:
            playerCharacter.UseItem()
        elif userInput in ["attack", "a", ""]:
            # Player attacks the enemy
            print(f"You swing your weapon at {enemy.mName}")
            hitChance = random.randint(0, 10)
            if hitChance > 3:
                # Successful attack
                Clear()
                enemy.AskiiArt()
                print (border)
                enemy.mHealth -= (playerCharacter.mDamage + randomDamage)
                print(f"Successful strike! Enemy health is now {enemy.mHealth}")
                if enemy.mHealth > 0:
                    # Enemy attacks if still alive
                    playerCharacter.mHealth -= round((enemy.mDamage + randomDamage) * playerCharacter.mDefence)
                    print(f"{enemy.mName} takes a swing and hits you. You now have {playerCharacter.mHealth} health.")
                else:
                    # Enemy defeated adds loot to player inventory
                    lootDropped = Loot(playerCharacter)
                    playerCharacter.mScore += enemy.mScore
                    print(f"You have defeated the {enemy.mName}. It looks like it dropped something:\nLoot: {lootDropped}\nScore: {playerCharacter.mScore}\n\n")
                    PressEnterToContinue()
                    break
            else:
                # Player misses the attack, leaving an opening for a counter-attack
                Clear()
                enemy.AskiiArt()
                print (border)
                print(f"You miss the {enemy.mName}, leaving an opening for a counter-attack.")
                playerCharacter.mHealth -= (enemy.mDamage + randomDamage)
                print(f"{enemy.mName} lands a full damage hit, ignoring your defense. Current health is {playerCharacter.mHealth}.")
                if playerCharacter.mHealth < 1:
                    break
        elif userInput in ["run away", "r"]:
            # Player attempts to run away
            Clear()
            enemy.AskiiArt()
            print (border)
            print(f"Neb: What you cant beat the {enemy.mName}, fine i'll open the gate, be carful though.")
            hitChance = random.randint(0, 10)
            if hitChance > 3 or enemy.mName == "Behemoth":
                # Successful escape
                print("Neb: You managed to escape, well done I guess, heres the key.")
                break
            else:
                # Failure to escape
                print(f"You tried to escape, but the {enemy.mName} was able to catch you. Your health: {playerCharacter.mHealth}.")
                playerCharacter.mHealth -= (enemy.mDamage + randomDamage)
                if playerCharacter.mHealth < 1:
                    break
        else:
            # Invalid userInput
            print(f"{userInput} not recognized.")

# Selects the challenge between riddle and combat, as well as if the room is the boss room
def Challenge(currentRoom, playerCharacter):
    # Check if there is an uncompleted challenge in the current room
    if currentRoom.mChallenge and not currentRoom.mChallenge["completed"]:
        Clear()
        print(f"{border}\nA challenge in {currentRoom.mLocation} awaits you.\n{border}")
        # Randomly select the type of challenge
        challengeType = random.choice(["riddle", "combat"])
        if currentRoom.mLocation == "Hidden Ritural Site":
            Combat(playerCharacter, currentRoom)
            return True
        elif challengeType == "riddle": 
            Riddle(playerCharacter)
        elif challengeType == "combat":
            Combat(playerCharacter, currentRoom)
        # Add the key obtained from the challenge to the player's key inventory
        playerCharacter.mKeys.append(currentRoom.mItem)
        # Mark the challenge as completed
        currentRoom.mChallenge["completed"] = True
    else:
        print(f"The challenge in {currentRoom.mLocation} has already been completed.")

# Random enemy generator
def RandomEnemySelector(currentRoom):
    randomEnemy = random.randint(1,4)
    # Checks if boss room then returns boss else you get a random enemy
    if currentRoom.mLocation == "Hidden Ritural Site" and currentRoom.mChallenge["completed"] == False:
        enemy = CCharacter("Behemoth", None, 100, None, 30, 0.3, None, 500, 1, 29)
    elif randomEnemy == 1:
        enemy = CCharacter("Gobblin", None, 40, None, 12, 0.10, None, 100, 162, 184)
    elif randomEnemy == 2:
        enemy = CCharacter("Demon", None, 40, None, 18, 0.25, None, 130, 29, 54)
    elif randomEnemy == 3:
        enemy = CCharacter("Lizard Man", None, 50, None, 16, 0.12, None, 150, 144, 162)
    elif randomEnemy == 4:
        enemy = CCharacter("Manticore", None, 70, None, 20, 0.28, None, 200, 54, 76)
    return enemy
    
# Random loot drops
def Loot(playerCharacter):
    # List of possible loot drops
    loot = ["health potion", "damage potion", "protection potion", "booster potion"]
    # Randomly selects a loot from the list
    lootChance = random.randint(0, 3)
    lootDropped = loot[lootChance]
    # Adds the loot to the player's inventory
    playerCharacter.AddToInventory(lootDropped)
    return lootDropped

# Selects a random riddle
def RandomRiddleSelector():
    randomRiddle = random.randint(1, 4)
    if randomRiddle == 1:
        riddle = CCharacter("What can't speak, but will speak\n when spoken to?", ["echo", "an echo"], None, None, "I bounce off the walls", None, None, 120, 184, 202)
        return riddle
    elif randomRiddle == 2:
        riddle = CCharacter("The more of this there is, the less you see.\n What is it?", ["darkness", "night"], None, None, "Close your eyes, what do you see?", None, None, 120, 184, 202)
        return riddle
    elif randomRiddle == 3:
        riddle = CCharacter("A man dies of old age on his 25th birthday.\n How is this possible?", ["he was born on a leap year", "he was born on February 29", "February 29", "leap year"], None, None, "Not every year has one", None, None, 120, 184, 202)
        return riddle
    elif randomRiddle == 4:
        riddle = CCharacter("I shave every day, but my beard stays\n the same. What am I?", ["barber", "hairdresser"], None, None, "You might visit them once or twice a month", None, None, 120, 184, 202)
        return riddle

# Riddle challange
def Riddle(playerCharacter):
    # Initialize userInput variable
    userInput = ""
    # Select a random riddle
    riddle = RandomRiddleSelector()
    # Continue looping until the player answers the riddle correctly or chooses to leave
    while userInput != riddle.mHero:
        PressEnterToContinue()
        riddle.AskiiArt()
        print(f"{border}you hear an annoying voice...{border}NEB: if you want the key riddle me this: {riddle.mName}")
        userInput = input("What is your answer?\n\nh: help\n\nt: tip\n\nl: leave\n\n>").lower()
        if userInput in ["help", "h"]:
            Help()
        elif userInput in riddle.mHero:
            # Add player's score and display correct answer message if the player's answer is correct
            playerCharacter.mScore += riddle.mScore
            print(f"Well done {playerCharacter.mName} you guessed correctly")
            break
        elif userInput in ["tip", "t"]:
            # Display a tip to help the player solve the riddle
            print(f"Struggling? Here's a tip: \n\n>{riddle.mDamage}\n")
        elif userInput in["leave", "l"]:
            print("Neb: Couldnt handle the riddle... fine i'll let you out, here's the key but you're not getting any points.")
            PressEnterToContinue()
            break
        else:
            print(f"{userInput} incorrect..Try again\n")
            
# Resets the challenge in each room
def ResetRooms():
    for room in rooms:
        rooms[room].mChallenge["completed"] = False
            
# Main function to run the game
def main():
    # Try except for error handaling, sending the user back to the main menu
    try:
        # Continue running the game until the user chooses to quit from the menu
        while True:
            playerCharacter = None
            currentRoom = None
            startTimer = None
            playerCharacter, currentRoom = Menu()
            startTimer = time.time()
            behemothDefeated = False
            ResetRooms()
            # Continue looping until the player's health reaches 0
            while playerCharacter.mHealth >= 0:
                # Clear the screen for each iteration of the game loop
                Clear()
                # Display the description of the current room
                currentRoom.DisplayLocationDescription()
                # Prompt the player to input a userInput
                userInput = input(f"\nType one of the following userInputs:\n\nChange room: {currentRoom.mDirections}\n\nL: Look\n\nS: Stats\n\nU: Use item\n\nH: Help\n\nE: Exit\n\n>").lower()
                # Process the player's input
                if userInput in ["help", "h"]:
                    Help()
                elif userInput in ["look", "l"]:
                    behemothDefeated = Challenge(currentRoom, playerCharacter)
                elif userInput in ["stats", "s"]:
                    playerCharacter.PlayerStats()
                    PressEnterToContinue()
                elif userInput in ["use item", "u"]:
                    playerCharacter.UseItem()
                elif userInput in currentRoom.mDirections:
                    currentRoom = currentRoom.Navigation(userInput, playerCharacter)
                elif userInput in ["exit", "e",]:
                    YeaOrNay("Are you Sure you want to  exit? (Y/N)")
                    break
                else:
                    print(f"{userInput} is not on of the options, please try again.")
                    PressEnterToContinue()
                # Check if the game is over after each loop
                isGameOver = GameOver(playerCharacter, behemothDefeated, startTimer)
                if isGameOver == False:
                    break
    except Exception as e:
        print(f"An error occurred: {e}")
        PressEnterToContinue()
        main()
if __name__ == "__main__":
    main()