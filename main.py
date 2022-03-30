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

#### ----VARIABLES---- ####
dhoaniCapacity = 0
supplierIslandAlphaCapacity = None
supplierIslandBetaCapacity = None
islandA_Capacity = 11690
islandB_Capacity = 13180
islandC_Capacity = 10200
islandD_Capacity = 10170
#### ----VARIABLES---- ####

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
island_a = []
islandA_ItemName = []
islandA_ItemAmount = []
# Lists for Island B Item Name and Item Amount.
island_b = []
islandB_ItemName = []
islandB_ItemAmount = []
# Lists for Island C Item Name and Item Amount.
island_c = []
islandC_ItemName = []
islandC_ItemAmount = []
# Lists for Island D Item Name and Item Amount.
island_d = []
islandD_ItemName = []
islandD_ItemAmount = []
#### ----LISTS---- ####

#### ----CLASSES---- ####
# This class will display Dhoani's drive and stop messages in the functions.
class DhoaniTravel:
    # Dhoani's function messages.
    drive = "Dhoani is travelling"
    stop = "Dhoani has stopped"

    # Dhoani's drive function.
    def get_drive(self):
        # Prints message of the Dhoani's function.
        return self.drive

    # Dhoani's stop function.
    def get_stop(self):
        # Prints message of the Dhoani's function.
        return self.stop

# This class will display different menu's needed for the program.
class Menu:
    # This function displays the main console menu.
    # Option 6 is continue and option 7 is quit.
    def consoleMenu():
        print("")
        print("---------------------------------")
        print("|      BigCon Construction      |")
        print("--------------Menu---------------")
        print("1- Add Items                    |")
        print("2- Remove Items                 |")
        print("3- Search Items                 |")
        print("4- Deliver Items                |")
        print("5- Print Items                  |")
        print("7- QUIT                         |")
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

    def deliverMenu():
        # Displays menu with destinations.
        print("---------------------------------")
        print("|      BigCon Construction      |")
        print("----------Destinations-----------")
        print("Island_A                        |")
        print("Island_B                        |")
        print("Island_C                        |")
        print("Island_D                        |")
        print("---------------------------------")
        

#### ----CLASSES---- ####

# Assigning class to a variable.
dhoani1 = DhoaniTravel()
menu1 = Menu()

#### ----FUNCTIONS---- ####
# This function checks the users specific choice and directs them to that function.
def consoleChoice(user_input):
    if user_input == 1:
        addItems()
    elif user_input == 2:
        removeItems()
    elif user_input == 3:
        searchItems()
    elif user_input == 4:
        deliverItems()
    elif user_input == 5:
        printItems()
    elif user_input == 7:
        exit()

# This function will add items.
def addItems():
    # Prints the Items Menu.
    print("")    
    menu1.itemsMenu()
    # Asks for user input.
    itemName = input("Item Name: ").lower()
    itemAmount = int(input("Item Amount: "))
    
    # Checks if Item Name and Item Amount is valid and adds it.
    if((itemName != ["diesel", "frozen", "fridge", "food", "protected material", "unprotected material"]) and (itemAmount > 30000)):
        print("INVALID INPUT")
    else:
        # Adds Item Name and Item Amount in the list.
        print("")
        print("----ADDING ITEM!----")
        # This will calculate and print the Dhoani's current capacity left.
        dhoaniCapacity = 30000
        capacityCalculate = dhoaniCapacity - itemAmount
        print("Current left: " + str(capacityCalculate) + "KG")
        dhoaniItemName.append(itemName)
        dhoaniItemAmount.append(itemAmount)
        
    # Asks user where to deliver.
    deliverItems()

    # Asks user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input("Continue (6) or Quit (7): "))
    print("")
    if user_input == 6:
        menu1.consoleMenu()
    else:
        exit()

# This function will remove items.
def removeItems():
    # Prints the Items Menu.
    print("")
    menu1.itemsMenu()
    # Asks for user input
    itemName = input("Item Name: ").lower()
    itemAmount = int(input("Item Amount: "))

    # Checks if Item Name and Item Amount is valid and removes it.
    if((itemName != ["diesel", "frozen", "fridge", "food", "protected material", "unprotected material"]) and (itemAmount > 30000)):
        print("INVALID INPUT")
    else:
        if ((itemName in dhoaniItemName) and (itemAmount in dhoaniItemAmount)):  
            # Removing Item Name and Item Amount.
            print("")
            print("----REMOVING ITEM!----")  
            # This will calculate and print the Dhoani's current capacity left.
            dhoaniCapacity = 30000
            capacityCalculate = dhoaniCapacity - itemAmount
            print("Capacity regained: " + str(capacityCalculate) + "KG")
            dhoaniItemName.remove(itemName)
            dhoaniItemAmount.remove(itemAmount)
            

            # Asking user if they wish to continue or quit.
            print("---------------------------------")
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
               menu1.consoleMenu()
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
        print("")
        print("----ITEM EXISTS!----")
        print("Item Name:", dhoaniItemName(user_input))
        print("Item Amount:", dhoaniItemAmount(user_input))
    else:
        # Error message.
        print("INVALID INPUT")

    # Asking user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input("Continue (6) or Quit (7): "))
    print("")
    if user_input == 6:
        menu1.consoleMenu()
    else:
        exit()

# This function will deliver items to destinations.
def deliverItems():
    
    user_input = input("Deliver to?: ").lower()

    # Checks what destination the user has chosen and displays where it goes.
    if user_input not in ["a", "b", "c", "d"]:
        # Error Message.
        print("INVALID INPUT")
    # Delivers to Island A.
    elif user_input in "a":
        island_a.append(dhoaniItemName)
        island_a.append(dhoaniItemAmount)
    # Delivers to Island B.
    elif user_input in "b":
        island_b.append(dhoaniItemName)
        island_b.append(dhoaniItemAmount)
    # Delivers to Island C.
    elif user_input in "c":
        island_c.append(dhoaniItemName)
        island_c.append(dhoaniItemAmount)
    # Delivers to Island D.
    elif user_input in "d":
        island_d.append(dhoaniItemName)
        island_d.append(dhoaniItemAmount)
    
# This function will print all of the lists and their amounts.
def printItems():
    # Dhoani inventory.
    print("")
    print("")
    print("")
    print("Dhoani Inventory")
    print("-----------------------------")
    print("Items: ", dhoaniItemName)
    print("Amount:", dhoaniItemAmount)
    print("-----------------------------")

    # Island A inventory.
    print("")
    print("Supply Island A Inventory")
    print("-----------------------------")
    print("All Items: ", island_a)
    #print("Items: ", islandA_ItemName)
    #print("Amount:", islandA_ItemAmount)
    print("-----------------------------")

    # Island B inventory.
    print("")
    print("Supply Island B Inventory")
    print("-----------------------------")
    print("All Items: ", island_b)
    #print("Items: ", islandB_ItemName)
    #print("Amount:", islandB_ItemAmount)
    print("-----------------------------")

    # Island C inventory.
    print("")
    print("Supply Island C Inventory")
    print("-----------------------------")
    print("All Items: ", island_c)
    print("Items: ", islandC_ItemName)
    print("Amount:", islandC_ItemAmount)
    print("-----------------------------")

    # Island D Inventory.
    print("")
    print("Supply Island D Inventory")
    print("-----------------------------")
    print("All Items: ", island_d)
    print("Items: ", islandD_ItemName)
    print("Amount:", islandD_ItemAmount)
    print("-----------------------------")

    # Asking user if they wish to continue or quit.
    user_input = int(input("Continue (6) or Quit (7): "))
    if user_input == 6:
        menu1.consoleMenu()
    else:
        exit()
#### ----FUNCTIONS---- ####

# Calling the function globally.
# Displays main console menu.
menu1.consoleMenu()

# PROGRAM END.
