"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: DADSA_ASSIGNMENT                            
Date: 10/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: DADSA year 02 Assignment - UWE Bristol BSc Computer Science
Student Number(UWE): 19045165
Student ID:(VC): 1802035                                       
Note: Uncomment codes to execute and comment them when not in use.                         
"""

# PROGRAM START.

#### ----LISTS---- ####
# Lists for Dhoani's Item Name and Item Amount.
dhoaniItemName = []
dhoaniItemAmount = []
# Lists for Supplier Island 01 Item Name and Item Amount.
supplierIslandAlphaItemName = []
supplierIslandAlphaItemAmount = []
# Lists for Supplier Island 02 Item Name and Item Amount.
supplierIslandBetaItemName = []
supplierIslandBetaItemAmount = []
# Lists for Island A Item Name and Item Amount.
islandA_ItemName = []
islandA_ItemAmount = []
# Lists for Island B Item Name and Item Amount.
islandB_ItemName = []
islandB_ItemAmount = []
# Lists for Island C Item Name and Item Amount.
islandC_ItemName = []
islandC_ItemAmount = []
# Lists for Island D Item Name and Item Amount.
islandD_ItemName = []
islandD_ItemAmount = []
#### ----LISTS---- ####

#### ----CLASSES---- ####
# This class will display Dhoani's drive and stop messages in the functions.
class DhoaniTravel:
    # Dhoani's function messages.
    drive = "Dhoani is driving"
    stop = "Dhoani has stopped"

    # Dhoani's drive function.
    def get_drive(self):
        # Prints message of the Dhoani's function.
        return self.drive

    # Dhoani's stop function.
    def get_stop(self):
        # Prints message of the Dhoani's function.
        return self.stop

#### ----CLASSES---- ####

# Assigning class to a variable.
dhoani1 = DhoaniTravel()

#### ----FUNCTIONS---- ####
# This function displays the main console menu.
# Option 5 is continue. If 6 is not chosen it selects 5.
def consoleMenu():
    print("")
    print("---------------------------------")
    print("|      BigCon Construction      |")
    print("--------------Menu---------------")
    print("1- Add Items                    |")
    print("2- Remove Items                 |")
    print("3- Search Items                 |")
    print("4- Print Items                  |")
    print("6- QUIT                         |")
    print("---------------------------------")

    # Asks for initial user input.
    user_input = int(input("Enter choice: "))
    consoleChoice(user_input)

# This function displays the Items Menu with their group code.
# Entering group code will not work. Enter the name displayed in the menu.
def itemsMenu():
    print("---------------------------------")
    print("|      BigCon Construction      |")
    print("--------------Items--------------")
    print("1- Diesel                       |")
    print("2- Frozen                       |")
    print("3- Fridge                       |")
    print("4- Food                         |")
    print("5- Protected Material           |")
    print("6- Unprotected Material         |")
    print("---------------------------------")

# This function displays the Destinations menu.
def destinationMenu():
    print("---------------------------------")
    print("|      BigCon Construction      |")
    print("----------Destinations-----------")
    print("Dhoani                          |")
    print("Supply Island 01                |")
    print("Supply Island 02                |")
    print("Island A                        |")
    print("Island B                        |")
    print("Island C                        |")
    print("Island D                        |")
    print("---------------------------------")

# This function checks the users specific choice and directs them to that function.
def consoleChoice(user_input):
    if user_input == 1:
        addItems()
    elif user_input == 2:
        removeItems()
    elif user_input == 3:
        searchItems()
    elif user_input == 4:
        printItems()
    elif user_input == 6:
        exit()

# This function will add items.
def addItems():
    # Prints the Items Menu.
    print("")    
    itemsMenu()
    # Asks for user input.
    itemName = input("Item Name: ").lower()
    itemAmount = int(input("Item Amount: "))

    # Checks if Item Name and Item Amount is valid and adds it.
    if((itemName != ["diesel", "frozen", "fridge", "food", "protected material", "unprotected material"]) and (itemAmount > 30000)):
        print("INVALID INPUT")
    else:
        # Adds Item Name and Item Amount in the list.
        print("----ADDING ITEM!----")  
        dhoaniItemName.append(itemName)
        dhoaniItemAmount.append(itemAmount)
        # Prints message of Dhoani travel function.
        print(dhoani1.get_drive())
        
    # Asks user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input("Continue (5) or Quit (6): "))
    print("")
    if user_input == 5:
        consoleMenu()
    else:
        exit()

# This function will remove items.
def removeItems():
    # Prints the Items Menu.
    print("")
    itemsMenu()
    # Asks for user input
    itemName = input("Item Name: ").lower()
    itemAmount = int(input("Item Amount: "))

    # Checks if Item Name and Item Amount is valid and removes it.
    if((itemName != ["diesel", "frozen", "fridge", "food", "protected material", "unprotected material"]) and (itemAmount > 30000)):
        print("INVALID INPUT")
    else:
        if ((itemName in dhoaniItemName) and (itemAmount in dhoaniItemAmount)):  
            # Removing Item Name and Item Amount.
            print("----REMOVING ITEM!----")  
            dhoaniItemName.remove(itemName)
            dhoaniItemAmount.remove(itemAmount)

            # Asking user if they wish to continue or quit.
            print("---------------------------------")
            user_input = int(input("Continue (5) or Quit (6): "))
            print("")
            if user_input == 5:
               consoleMenu()
            else:
               exit()
        else:
            # Error message.
            print("INVALID INPUT")

# This function will search through the lists and print items and their amounts.
def searchItems():
    print("----SEARCHING ITEMS----")
    print("---------------------------------")
    itemName = input("Item Name: ")
    itemAmount = int(input("Item Amount: "))
    
    # Checks if the entered elements exists in the lists and prints them.
    if ((itemName in dhoaniItemName) and (itemAmount in dhoaniItemAmount)):
        print()
        print("----ITEM EXISTS!----")
        print("Item Name:", dhoaniItemName)
        print("Item Amount:", dhoaniItemAmount)
    else:
        # Error message.
        print("INVALID INPUT")

    # Asking user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input("Continue (5) or Quit (6): "))
    print("")
    if user_input == 5:
        consoleMenu()
    else:
        exit()

# This function will print all of the lists and their amounts.
def printItems():
    # Dhoani inventory.
    print("")
    print("Dhoani Inventory")
    print("-----------------------------")
    print("Items: ", dhoaniItemName)
    print("Amount:", dhoaniItemAmount)
    print("-----------------------------")

    # Supply Island inventory.
    print("")
    print("Supply Island 01 Inventory")
    print("-----------------------------")
    print("Items: ", supplierIslandAlphaItemName)
    print("Amount:", supplierIslandAlphaItemAmount)
    print("-----------------------------")

    # Supply Island 02 inventory.
    print("")
    print("Supply Island 02 Inventory")
    print("-----------------------------")
    print("Items: ", supplierIslandBetaItemName)
    print("Amount:", supplierIslandBetaItemAmount)
    print("-----------------------------")

    # Island A inventory.
    print("")
    print("Supply Island A Inventory")
    print("-----------------------------")
    print("Items: ", islandA_ItemName)
    print("Amount:", islandA_ItemAmount)
    print("-----------------------------")

    # Island B inventory.
    print("")
    print("Supply Island B Inventory")
    print("-----------------------------")
    print("Items: ", islandB_ItemName)
    print("Amount:", islandB_ItemAmount)
    print("-----------------------------")

    # Island C inventory.
    print("")
    print("Supply Island C Inventory")
    print("-----------------------------")
    print("Items: ", islandC_ItemName)
    print("Amount:", islandC_ItemAmount)
    print("-----------------------------")

    # Island D Inventory.
    print("")
    print("Supply Island D Inventory")
    print("-----------------------------")
    print("Items: ", islandD_ItemName)
    print("Amount:", islandD_ItemAmount)
    print("-----------------------------")

    # Asking user if they wish to continue or quit.
    user_input = int(input("Continue (5) or Quit (6): "))
    if user_input == 5:
        consoleMenu()
    else:
        exit()
#### ----FUNCTIONS---- ####

# Calling the function globally.
# Displays main console menu.
consoleMenu()

# PROGRAM END.
