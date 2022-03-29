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

#### ----FUNCTIONS---- ####
# This function displays the main console menu.
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

# This function displays the Destinations Menu.
def destinationMenu():
    print("---------------------------------")
    print("|      BigCon Construction      |")
    print("---------------------------------")
    print("Dhoani                          |")
    print("Supply Island 01                |")
    print("Supply Island 02                |")
    print("Island A                        |")
    print("Island B                        |")
    print("Island C                        |")
    print("Island D                        |")
    print("---------------------------------")

# This function checks the users specific choice and directs to that function.
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
        
    # Asks user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input("Continue (5) or Exit (6): "))
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
            user_input = int(input("Continue (5) or Exit (6): "))
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
    user_input = int(input("Continue (5) or Exit (6): "))
    print("")
    if user_input == 5:
        consoleMenu()
    else:
        exit()

# This function will print all of the lists and their amounts.
def printItems():
    print("")
    print("Dhoani Inventory")
    print("-----------------------------")
    print("Items: ", dhoaniItemName)
    print("Amount:", dhoaniItemAmount)
    print("-----------------------------")

    # Asking user if they wish to continue or quit.
    user_input = int(input("Continue (5) or Exit (6): "))
    if user_input == 5:
        consoleMenu()
    else:
        exit()
#### ----FUNCTIONS---- ####

# Calling the function globally.
# Displays main console menu.
consoleMenu()

# PROGRAM END.
