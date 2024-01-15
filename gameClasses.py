
from gameFunctions import clear, pressEnterToContinue

border = ("\n<------------------------------------------------------------------------------------------>\n")

class Ccharacter:
    def __init__(self, name, characterType, hp, mp, attack, skill, inventory):
        self.mName = name
        self.mCharacterType = characterType
        self.mHp = hp
        self.mAttack = attack
        self.mSkill = skill
        self.mInventory = inventory
        
    def showStats(self):
        clear()
        print(f"{border}"
              f"\nName: {self.mName}"
              f"\nClass: {self.mCharacterType}"
              f"\nHP: {self.mHp}"
              f"\nMP: {self.mMp}"
              f"\nAttack: {self.mAttack}"
              f"\nSkill: {self.mSkill}"
              f"\nInventory: {self.mInventory}")

    def showHpMp(self):
        print(f"{border}"
              f"\nHP: {self.mHp}"
              f"\nMP: {self.mMp}")

    def useItem(self):
        clear()
        print (border)
        self.mInventory()
        Itemconsumed = input("What item would you like to use:\n").lower()

class CEnemy:
    def __init__(self, name, hp, attack, inventory):
        self.mName = name
        self.mHp = hp
        self.mAttack = attack
        self.mInventory = inventory

    def showStats(self):
        clear()
        print(f"{border}"
              f"\nName: {self.mName}\n"
              f"\nHP: {self.mHp}\n"
              f"\nAttack: {self.mAttack}\n"
              f"\nInventory: {self.mInventory}\n")

#Creates a border 130 characters long, loops text and places borders on the sides
class UserInterface:
    def __init__(self, lineLength=130):
        self.lineLength = lineLength
        self.border = "<" + "-" * lineLength + ">"

    def textLoopBorder(self, text):
        def textLoop(text):
            words = text.split()
            lines = []
            currentLine = ""

            for word in words:
                if len(currentLine) + len(word) + 1 <= self.lineLength:
                    currentLine += word + " "
                else:
                    lines.append(currentLine.strip())
                    currentLine = word + " "

            if currentLine:
                lines.append(currentLine.strip())

            borderedLines = [f"|{line.center(self.lineLength)}|" for line in lines]
            return f"{self.border}\n{'\n'.join(borderedLines)}\n{self.border}"

        return textLoop(text)

class currentLocation:
    def __init__(self, description):
        self.description = description
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
        return item
    
    def displayDescription(self):
        formattedDescription = UserInterface.textLoopBorder(self.description)
        print(formattedDescription)

enchantedForest = currentLocation("Surrounded by tall, dark trees, you stand in a mystical forest. Blue leaves gently descend"
        "from the sky, casting an ethereal glow upon the surroundings. The air is filled with"
        "enchantment as the magical foliage paints the scene with its serene illumination.",)
enchantedForest.addItem("twinkling twig")

frozenStoneGarden = currentLocation("In this frigid landscape, an intense cold envelops everything. Frozen statues dot the"
        "\nsurroundings, revealing upon closer examination that they are not sculptures but the chilling"
        "\nfate of people and creatures caught in an icy stasis. The profound stillness of this frozen"
        "\nrealm conceals the silent stories of those who succumbed to the relentless grip of cold.")
frozenStoneGarden.addItem("frozen faucet")

floodedAlcemyRoom = currentLocation("Vivid hues of moss and slime coat the walls, creating a surreal tapestry of colors. The floor,"
        "\nobscured by an unseen flood, bears witness to a chemical concoction that has transformed the"
        "\nenvironment into a mesmerizing yet mysterious spectacle. The amalgamation of diverse chemicals"
        "\nbeneath contributes to a uniquely vibrant and enigmatic atmosphere within these walls.")
floodedAlcemyRoom.addItem("pungent potion")

magicalLibariy = currentLocation("A whirlwind of books fills the air, with each tome rising from a pile on the ground,"
        "\nfloating gracefully to find its place on an infinite bookcase. Yet, the cycle repeats as"
        "\nthe books descend, creating a mesmerizing and perpetual dance of literature. The never-ending"
        "\nspectacle captures the essence of an unending cycle, where knowledge and stories take flight"
        "\nonly to return and continue their enchanting journey.")
magicalLibariy.addItem("blazing book")

hiddenRituralSite = currentLocation("As you tread through the secretive ceremonial grounds, an unexpected revelation unfolds—the"
        "\nimposing Boss emerges from the shadows. This pivotal encounter marks a turning point,"
        "\npromising both challenges and profound revelations within the mysterious heart of this"
        "\nconcealed sanctuary.")


enchantedForest.west = frozenStoneGarden
frozenStoneGarden.north = floodedAlcemyRoom
frozenStoneGarden.east = enchantedForest
frozenStoneGarden.south = magicalLibariy
frozenStoneGarden.west = hiddenRituralSite
floodedAlcemyRoom.south = frozenStoneGarden
magicalLibariy.north = frozenStoneGarden
hiddenRituralSite.east = frozenStoneGarden

print(enchantedForest.description)

current_Location = enchantedForest

