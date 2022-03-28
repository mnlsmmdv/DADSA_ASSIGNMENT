"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: DADSA                            
Date: 10/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: DADSA year 02 Assignment
Student ID: S1802035                                       
Note: Uncomment codes to execute and comment them when not in use.                         
"""

# PROGRAM START.

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

# This function displays the main console menu.
def consoleMenu():
    print("---------------------------------")
    print("|      BigCon Construction      |")
    print("--------------Menu---------------")
    print("1- Add Items                    |")
    print("2- Remove Items                 |")
    print("3- Update Items                 |")
    print("4- Search Items                 |")
    print("5- Print Items                  |")
    print("7- QUIT                         |")
    print("---------------------------------")

    # Asks for initial user input.
    user_input = int(input("Enter choice: "))
    consoleChoice(user_input)

# This function displays the Items Menu with their group code.
def itemsMenu():
    print("---------------------------------")
    print("|      BigCon Construction      |")
    print("--------------Menu---------------")
    print("1- Diesel                       |")
    print("2- Frozen                       |")
    print("3- Fridge                       |")
    print("4- Food                         |")
    print("5- Protected Material           |")
    print("6- Unprotected Material         |")
    print("---------------------------------")

# This function checks the users specific choice and directs to that function.
def consoleChoice(user_input):
    if user_input == 1:
        addItems()
    elif user_input == 2:
        removeItems()
    elif user_input == 3:
        updateItems()
    elif user_input == 4:
        searchItems()
    elif user_input == 5:
        printItems()
    elif user_input == 7:
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
        dhoaniItemName.append(itemName)
        dhoaniItemAmount.append(itemAmount)
        
    # Asks user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input('Enter 6 to continue or 7 to exit: '))
    print("")
    if user_input == 6:
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
            print("REMOVING ITEM!")  
            dhoaniItemName.remove(itemName)
            dhoaniItemAmount.remove(itemAmount)

            # Asks user if they wish to continue or quit.
            print("---------------------------------")
            user_input = int(input("Enter 6 to continue or 7 to exit: "))
            print("")
            if user_input == 6:
               consoleMenu()
            else:
               exit()
        else:
            # Error message.
            print("INVALID INPUT")

# This function will update the elements in the list.
def updateItems():
    print("Updating Inventory")
    print("---------------------------------")
    itemName = input('Item Name: ')
    itemAmount = int(input("Item Amount: "))
    
    # Checks if Item Name and Item Amount is valid and updates it.
    if((itemName != ["diesel", "frozen", "fridge", "food", "protected material", "unprotected material"]) and (itemAmount > 30000)):
        print("INVALID INPUT")
    else:
        if ((itemName in dhoaniItemName) and (itemAmount in dhoaniItemAmount)):  
            # Removing Item Name and Item Amount.
            print("REMOVING ITEM!")  
            dhoaniItemName.append(itemName)
            dhoaniItemAmount.append(itemAmount)

            # Asking user if they wish to continue.
            print("---------------------------------")
            user_input = int(input("Enter 6 to continue or 7 to exit: "))
            print("")
            if user_input == 6:
               consoleMenu()
            else:
               exit()
        else:
            # Error message.
            print("INVALID INPUT")

# This function will search through the lists and print it.
def searchItems():
    print('Searching Inventory')
    print("---------------------------------")
    itemName = input('Item Name: ')
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

    # Asking user if they wish to continue.
    print("---------------------------------")
    user_input = int(input("Enter 6 to continue or 7 to exit: "))
    print("")
    if user_input == 6:
        consoleMenu()
    else:
        exit()

# This function will print all of the lists and their amounts.
def printItems():
    print('Dhoani Inventory')
    print("-----------------------------")
    print("Items: ", dhoaniItemName)
    print("Amount:", dhoaniItemAmount)
    print("-----------------------------")

    # Asks user if they wish to continue or quit.
    user_input = int(input('Enter 6 to continue or 7 to exit: '))
    if user_input == 6:
            consoleMenu()
    else:
        exit()

# Calling the function globally.
# Displays main console menu.
consoleMenu()

# PROGRAM END.
