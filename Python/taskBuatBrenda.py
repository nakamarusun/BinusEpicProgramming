from os import system, name
from time import sleep
from sys import exit
import random

class Contents():
    name: str = ""
    amount: int = 0

    def __init__(self, name: str, amount: int = 1):
        self.name = name
        self.amount = amount

class Food(Contents):
    needCool = True

class NonFood(Contents):
    needCool = False

class Storage():
    content: [Contents] = []
    capacity: int = 0
    name: str

    def __init__(self, name, capacity = 3):
        self.name = name
        self.capacity = capacity
        self.content = []

    def addObject(self, put: Contents):
        inFridge = False
        for i in self.content:
            if i.name == put.name:
                i.amount += put.amount
                inFridge = True
                break
        if inFridge == False:
            if len(self.content) < self.capacity:
                self.content.append(put)
                return True
            else:
                print("Storage full ! Remove some items !")
        return False

class Freezer(Storage):
    content: [Contents] = []
    refreshing = True
    capacity: int

    def __init__(self, name, capacity = 3):
        super().__init__(name, capacity)

    def drawFridge(self):

        print("    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ")
        print(" ▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓ ")
        print("▓▓▓▒▒░░░░                ░░░░▒▒▓▓▓")
        print("▓▒░░        Das Freezer       ░░▒▓")           # there are 29 whitespaces
        
        for i in self.content:

            print("▓▒░                            ░▒▓")
            print("▓                                ▓")
            strDesc = i.name + ": " + str(i.amount) + " @ " + str(int(100)) + "%"
            strLen = len(strDesc)
            whiteLeft = 29 - strLen
            if whiteLeft < 0:
                whiteLeft = 0
            print("▓", end = "")
            if whiteLeft % 2 == 0:
                print(" " * (whiteLeft // 2), strDesc, " " * (whiteLeft // 2), "▓")
            else:
                print(" " * (whiteLeft // 2 + 1), strDesc, " " * (whiteLeft // 2), "▓")
            
            print("▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓")
        
        print("▓                                ▓")
        print("▓░                              ░▓")
        print("▓▒░░░░░                    ░░░░░▒▓")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

class Shelf(Storage):
    content: [Contents] = []
    refreshing = False
    capacity: int

    def __init__(self, name, capacity = 5):
        super().__init__(name, capacity)
    
    def drawFridge(self):

        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("▓▓▒▒         Das Shelf        ▒▒▓▓")
        print("▓▓▒                            ▒▓▓")
        for i in self.content:
            print("▓▓                              ▓▓")
            print("▓▓                              ▓▓")
            strDesc = i.name + ": " + str(i.amount) + " @ " + str(int(100)) + "%"
            strLen = len(strDesc)
            whiteLeft = 27 - strLen
            if whiteLeft < 0:
                whiteLeft = 0
            print("▓▓", end = "")
            if whiteLeft % 2 == 0:
                print(" " * (whiteLeft // 2), strDesc, " " * (whiteLeft // 2), "▓▓")
            else:
                print(" " * (whiteLeft // 2 + 1), strDesc, " " * (whiteLeft // 2), "▓▓")

            print("▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓")

        print("▓▓▒                            ▒▓▓")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def printTitle():
    print("   THE")
    print("  █████▒██▀███   ██▓▓█████▄   ▄████ ▓█████      ██████  ██▓ ███▄ ▄███▓ █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  ")
    print("▓██   ▒▓██ ▒ ██▒▓██▒▒██▀ ██▌ ██▒ ▀█▒▓█   ▀    ▒██    ▒ ▓██▒▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒")
    print("▒████ ░▓██ ░▄█ ▒▒██▒░██   █▌▒██░▄▄▄░▒███      ░ ▓██▄   ▒██▒▓██    ▓██░▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒")
    print("░▓█▒  ░▒██▀▀█▄  ░██░░▓█▄   ▌░▓█  ██▓▒▓█  ▄      ▒   ██▒░██░▒██    ▒██ ▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ")
    print("░▒█░   ░██▓ ▒██▒░██░░▒████▓ ░▒▓███▀▒░▒████▒   ▒██████▒▒░██░▒██▒   ░██▒▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒")
    print("▒ ░   ░ ▒▓ ░▒▓░░▓   ▒▒▓  ▒  ░▒   ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░")
    print("░       ░▒ ░ ▒░ ▒ ░ ░ ▒  ▒   ░   ░  ░ ░  ░   ░ ░▒  ░ ░ ▒ ░░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░")
    print("░ ░     ░░   ░  ▒ ░ ░ ░  ░ ░ ░   ░    ░      ░  ░  ░   ▒ ░░      ░    ░░░ ░ ░   ░ ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ ")
    print("        ░      ░     ░          ░    ░  ░         ░   ░         ░      ░         ░  ░     ░  ░            ░ ░     ░    ")
    print()
    print("v1.0 by jason")

def intro():
    printTitle()
    sleep(2)
    for i in range(3):
        print()

    print("Welcome to The Fridge Simulator !")
    print()
    print("You currently have one fridge and one shelf. You have also 0 money.")
    print("Money can be earned by playing the game and putting the objects correctly to which storage containers.")
    print("You objective is to put food items that can rot (ex. Mango) to the fridge, and the others to the shelf.")
    print("The fridge has a storage of 3 items, and the shelf has a storage of 5.")
    print("If you start running out of storage, you have to buy more storage or you will LOSE THE GAME.")

    while True:
        print()
        prompt = input("Type 'Y' and enter to play the game. (Y/N): ")
        if prompt == "y" or prompt == "Y":
            break
        elif prompt == "n" or prompt == "N":
            exit(0)

def selectStorage(arg: str) -> Storage:
    print()
    print("Fridges:")
    print("Select the storage in which you want to", arg)

    for i in range(len(myFridges)):
        print(str(i + 1) + "a. " + myFridges[i].name)
    print()
    print("Shelves:")

    for i in range(len(myShelves)):
        print(str(i + 1) + "b. " + myShelves[i].name)

    while True:
        try:
            prompt = input("Enter alphanum (or exit to exit): ")
            if len(prompt) == 2:
                if prompt[1].lower() == "a":
                    return myFridges[int(prompt[0]) - 1]
                elif prompt[1].lower() == "b":
                    return myShelves[int(prompt[0]) - 1]
            elif prompt.lower() == "exit":
                break
        except:
            print("Invalid input. Press enter to reenter value")
            print()

def showStatus():
    print("▒  ▒ ▒▒  ▒▒ ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒ ▒▒  ▒ ▒   ▒")
    print("                             Money: $" + str(money) + "     Fridges: " + str(len(myFridges)) + "     Shelves: " + str(len(myShelves)))

def viewContainer() -> bool:
    clear()
    showStatus()
    try:
        selectedStorage = selectStorage("view.")
    except:
        print("Invalid input.")
        input("Press enter to continue..")
        return False

    clear()
    showStatus()
    print()
    print()
    try:
        selectedStorage.drawFridge()
    except:
        input("Press enter to go back..")
        return False
    input("Press enter to go back..")
    return True

def storeContainer(item, amnt: int):
    clear()
    showStatus()
    try:
        selectedStorage = selectStorage("store.")
    except:
        print("Invalid input.")
        input("Press enter to continue..")
        return False
    print()
    print()
    newItem = item
    for i in selectedStorage.content:
        if i.name.lower() == newItem.name.lower():
            i.amount += amnt
            print()
            print("Stored", newItem.name, ":", amnt, "in", selectedStorage.name, "!")
            print()
            input("Press any key and enter to go back..")
            return True, selectedStorage
    newItem.amount = amnt
    if selectedStorage.addObject(newItem):
        print()
        print("Stored", newItem.name, ":", amnt, "in", selectedStorage.name, "!")
        print()
        input("Press any key and enter to go back..")
        return True, selectedStorage
    print()
    input("Fridge is full ! failed to store")
    return False

def takeContainer():
    clear()
    showStatus()
    try:
        selectedStorage = selectStorage("take from.")
    except:
        print("Invalid input.")
        input("Press enter to continue..")
        return False
    clear()
    showStatus()
    print()
    selectedStorage.drawFridge()
    print()
    itemTaken = input("enter the item you want to take: ")
    for i in range(len(selectedStorage.content)):
        if itemTaken.lower() == selectedStorage.content[i].name.lower():
            while True:
                try:
                    amnt = int(input("Enter quantity of item: "))
                    if amnt <= 0:
                        print("You can't do that..")
                        input("Press enter to continue..")
                        return False
                    break
                except:
                    pass
            if amnt > selectedStorage.content[i].amount:
                print("You are taking too many items.")
                input("Press enter to continue..")
                return False
            elif amnt < selectedStorage.content[i].amount:
                selectedStorage.content[i].amount -= amnt
                print("Took", amnt, "of", selectedStorage.content[i].name, "!")
                input("Press enter to continue..")
                return True, selectedStorage.content[i].name, amnt
            else:
                returnVal = selectedStorage.content[i]
                del selectedStorage.content[i]
                print("Took", amnt, "of", returnVal.name, "!")
                input("Press enter to continue..")
                return True, returnVal.name, amnt

def buyContainer(money) -> int:
    while True:
        clear()
        showStatus()
        print("Do you want to buy a fridge, or a shelf ?")
        print()
        print("1. Fridge: $200")
        print("2. Shelf: $150")
        print()
        prompt = input("Choose (Exit to exit): ")
        if prompt == "1" and money >= 200:
            prompt = input("Give it a name: ")
            myFridges.append(Freezer(prompt))
            input("Buy success ! press enter to continue..")
            money -= 200
            return 1
        elif prompt == "2" and money >= 150:
            prompt = input("Give it a name: ")
            myFridges.append(Freezer(prompt))
            input("Buy success ! press enter to continue..")
            money -= 150
            return 2
        elif prompt.lower() == "exit":
            return 0
        else:
            print("You do not have enough money !")
            input("Press enter to continue")
            return 0

global money

money = 0
myFridges: [Freezer] = []
myShelves: [Shelf] = []

foods: [Food] = []
nonFoods: [NonFood] = []

myFridges.append(Freezer("Standard Fridge"))
myShelves.append(Shelf("Standard shelf"))

foodNames = ("Orange", "Chicken", "Beef", "Pizza", "Milk", "Avocado", "Eggs", "Cheese", "Sliced Melons", "Butter", "Yogurt from Cimori™", "Salad", "Ice", "Lemons")
nonFoodNames = ("Scissors", "Bottle", "Salt", "Knife", "Spoon", "Fork", "Spork", "Board", "Napkin", "Plates", "Bowl", "Elephant")

for i in foodNames:
    foods.append(Food(i))

for i in nonFoodNames:
    nonFoods.append(NonFood(i))

randomize = True
inHand = False

global curItem
global curQuantity

clear()
intro()

while True:
    clear()
    showStatus()
    print()
    print()
    if randomize:
        if random.randint(0, 1) == 1:
            curItem = foods[random.randint(0, len(foods) - 1)]
        else:
            curItem = nonFoods[random.randint(0, len(nonFoods) - 1)]
        curQuantity = random.randint(1, 13)
        randomize = False
    if not inHand:
        print("A packet just arrived !", curQuantity, curItem.name, "is in it. What do you want to do ?")
    else:
        print("You have", curQuantity, curItem.name, "in your hand. What do you want to do ?")
    print()
    print("View: view the content of your fridge or shelf.")
    print("Store: store the item in the correct container.")
    if not inHand:
        print("Take: take an item in a container and move it somewhere else.")
    print("Buy: buy a new shelf or fridge to store more items.")
    print()
    prompt = input("(View/Store/Take/Buy): ") if not inHand else input("(View/Store/Buy): ")
    if prompt.lower() ==  "view":
        viewContainer()
    elif prompt.lower() == "store":
        newItem = curItem
        if curItem.name in foodNames:
            newItem = Food(curItem.name)
        elif curItem.name in nonFoodNames:
            newItem = NonFood(curItem.name)
        try:
            truth, select = storeContainer(newItem, curQuantity)
            if select.refreshing and not inHand:
                for i in foodNames:
                    if i == curItem.name:
                        money += 50
            elif not select.refreshing and not inHand:
                for i in nonFoodNames:
                    if i == curItem.name:
                        money += 50
            if truth:
                randomize = True
                inHand = False
        except:
            pass
    elif prompt.lower() == "take":
        if not inHand:
            try:
                a, b, c = takeContainer()
                if a == True:
                    curQuantity = c
                    inHand = True
                    if b in foodNames:
                        curItem = foods[foodNames.index(b)]
                    elif b in nonFoodNames:
                        curItem = nonFoods[nonFoodNames.index(b)]
            except:
                print("Invalid input !")
                input("Press enter to continue..")
        else:
            print("There is something in your hand ! can not take anymore !")
            input("Press enter to continue..")
    elif prompt.lower() == "buy":
        val = buyContainer(money)
        if val == 1:
            money -= 200
        elif val == 2:
            money -= 150