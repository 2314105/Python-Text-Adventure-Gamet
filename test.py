import os
import random
import time

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

# Character class
class CCharacter:
    def __init__(self, name, hero, health, magic, damage, defence,):
        self.mName = name
        self.mHero = hero
        self.mHealth = health
        self.mMagic = magic
        self.mDamage = damage
        self.mDefence = defence
        self.mInventory = []

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
        
#Displays gameover screen based on players health
def gameOver(playerCharacter, mScore):
    if playerCharacter.mHealth < 1:
        print(f"Score = {mScore}")
        print("You lose Sucker!!!")

#
def characterName():
    while True:
        name = input("Tell me Hero, What is thy Name\n\n>").capitalize()
        if 3 <= len(name) <= 10:
            confirm_name = yeaOrNay(f"{border} Is {name} your Name Yae/Nay: \n\n")
            if confirm_name:
                return name
        else:
            print("\nInvalid name length. Your name should be between 4 and 10 characters.")
            input(f"{border}Press enter to try again{border}\n>")

def characterCreator():
        name = characterName()
        while True:
            clear()
            while True:
                command = input(f"{name}, What type of hero are you?\n1. warrior\n\n2. mage\n\n3. rogue").lower()
                if command in ["warrior", "one", "1"]:
                    character = CCharacter(name, "Warrior", 100, 6, 15, 10)
                    break
                elif command in ["mage", "two", "2"]:
                    character = CCharacter(name, "Mage", 80, 18, 7, 4)
                    break
                elif command in ["rogue", "three", "3"]:
                    character = CCharacter(name, "Rogue", 60, 20, 24, 2)
                    break

            character.playerStats()
            command = yeaOrNay(f"{border} Is this your class Yae/Nay: \n\n")
            if command:
                return character

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
    
def loot():
    loot = ["Health potion", "Damage Potion", "Defence potion"]
    lootChance = random.randint(0,2)
    lootDropped = loot[lootChance]
    return lootDropped

def mScore(enemy, currentScore):
    updatedScore =currentScore + enemy.mMagic
    return updatedScore

def combat(playerCharacter, currentScore):
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
                    currentScore = mScore(enemy, currentScore)
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
                    currentScore = mScore(enemy, currentScore)
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

def main():
        mScore = 0
        playerCharacter = characterCreator()
        combat(playerCharacter, mScore)
if __name__ == "__main__":
    main()


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