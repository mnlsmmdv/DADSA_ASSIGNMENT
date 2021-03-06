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
supplierIslandAlpha = []
# Lists for Supplier Island 02 Item Name and Item Amount.
supplierIslandBeta = []
# Lists for Island A Item Name and Item Amount.
islandA_ItemName = []
islandA_ItemAmount = []
#islandA = islandA_ItemName + islandA_ItemAmount
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
# This class will display Dhoani's drive and stop messages also the various menu's needed for this program.
class MENU_AND_TRAVEL:
    # Dhoani's function messages.
    drive = "Dhoani is now travelling to "
    stop = "Dhoani has stopped at "

    # Dhoani's drive function.
    def get_drive(self):
        # Prints message of the Dhoani's function.
        return self.drive

    # Dhoani's stop function.
    def get_stop(self):
        # Prints message of the Dhoani's function.
        return self.stop

    # This function displays the main console menu.
    # Option 6 is continue and option 7 is quit.
    def consoleMenu(self):
        print("")
        print("")
        print("---------------------------------")
        print("|      BigCon Construction      |")
        print("--------------Menu---------------")
        print("1- Add Items                    |")
        print("2- Remove Items                 |")
        print("3- Search Items                 |")
        print("4- Deliver Items                |")
        print("5- Print Items                  |")
        print("7- QUIT PROGRAM                 |")
        print("---------------------------------")
    
        # Asks for initial user input.
        user_input = int(input("Enter choice: "))
        consoleChoice(user_input)

    # This function displays the Items Menu with their group code.
    # Entering group code will not work. Enter the name displayed in the menu.
    def itemsMenu(self):
        print("")
        print("")
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
    
    # This function displays the Deliver Items menu and their destination names.
    # Displays menu with destinations.
    def deliverMenu(self):
        print("")
        print("")
        print("---------------------------------")
        print("|      BigCon Construction      |")
        print("----------Destinations-----------")
        print("Island A                        |")
        print("Island B                        |")
        print("Island C                        |")
        print("Island D                        |")
        print("---------------------------------")
#### ----CLASSES---- ####

# Assigning class to variables.
menu_and_travel = MENU_AND_TRAVEL()

#### ----FUNCTIONS---- ####
# This function checks the users specific choice and directs them to that function.
def consoleChoice(user_input):
    # Add items.
    if user_input == 1:
        addItems()
    # Remove items.
    elif user_input == 2:
        removeItems()
    # Search items.
    elif user_input == 3:
        searchItems()
    # Deliver items.
    elif user_input == 4:
        deliverItems()
    # Print items.
    elif user_input == 5:
        printItems()
    # Quit program.
    elif user_input == 7:
        exit()
    # Invalid option.
    else:
        print("INVALID OPTION")
        menu_and_travel.consoleMenu()

# This function will add items.
def addItems():
    # Prints the Items Menu and asks for user input.
    print("")    
    menu_and_travel.itemsMenu()

    # Validates item name.
    itemName = input("Item Name: ").lower()    
    if itemName not in ["diesel", "frozen", "fridge", "food", "protected material", "unprotected material"]:
        # Error message.
        print("INVALID ITEM")
    
    # Validates item amount.
    itemAmount = int(input("Item Amount: "))
    if itemAmount >= 30000:
        print("INVALID AMOUNT")
    else:
        print("---------------------------------")
        #print("Capacity Reaced!")
        print("----ADDING ITEM!----")
        # This will calculate and print the Dhoani's current capacity left.
        dhoaniCapacity = 30000
        capacityCalculate = dhoaniCapacity - itemAmount
        print("Capacity left: " + str(capacityCalculate) + "KG")
        # Adds item name and item amount
        dhoaniItemName.append(itemName)
        dhoaniItemAmount.append(itemAmount)
        # Asks user if they wish to add another item. If not exits.
        print("---------------------------------")
        user_input = input("Add another item?(yes/no): ").lower()
        print("---------------------------------")
        if(user_input in "yes"):
            menu_and_travel.consoleMenu()
        
        if(user_input in "no"):
            deliverItems()
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
                menu_and_travel.consoleMenu()
            else:
                exit()
           
    # Prints the Deliver Items Menu.
    deliverItems()

    # Asks user if they wish to continue or quit.
    print("---------------------------------")
    user_input = int(input("Continue (6) or Quit (7): "))
    print("")
    if user_input == 6:
        menu_and_travel.consoleMenu()
    else:
        exit()

# This function will remove items from the dhoani after it has been delivered.
def removeItems():
    # Prints the Items Menu and asks for user input.
    print("")
    menu_and_travel.itemsMenu()
    itemName = input("Item Name: ").lower()
    itemAmount = int(input("Item Amount: "))
    from_remove = input("From: ").lower()

    # Checks if Item Name and Item Amount is valid and removes it.
    if from_remove == "dhoani":
        print("")
        print("----REMOVING ITEM!----")
        dhoaniItemName.remove(itemName)
        dhoaniItemAmount.remove(itemAmount)
        user_input = input("Remove another item?(yes/no): ").lower()
        print("---------------------------------")
        if user_input == "yes":
            menu_and_travel.consoleMenu()
        else:
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
                menu_and_travel.consoleMenu()
            else:
                exit()
    
    # Checks if Item Name and Item Amount is valid and removes it.
    elif from_remove == "island a":
        print("")
        print("----REMOVING ITEM!----")
        print("-----CONSUMPTION------")
        islandA_ItemName.remove(dhoaniItemName)
        islandA_ItemAmount.remove(dhoaniItemAmount)
        user_input = input("Remove another item?(yes/no): ").lower()
        print("---------------------------------")
        if user_input == "yes":
            menu_and_travel.consoleMenu()
        else:
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
                menu_and_travel.consoleMenu()
            else:
                exit()

    # Checks if Item Name and Item Amount is valid and removes it.
    elif from_remove == "island b":
        print("")
        print("----REMOVING ITEM!----")
        print("-----CONSUMPTION------")
        islandB_ItemName.remove(dhoaniItemName)
        islandB_ItemAmount.remove(dhoaniItemAmount)
        user_input = input("Remove another item?(yes/no): ").lower()
        print("---------------------------------")
        if user_input == "yes":
            menu_and_travel.consoleMenu()
        else:
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
                menu_and_travel.consoleMenu()
            else:
                exit()

    # Checks if Item Name and Item Amount is valid and removes it.
    elif from_remove == "island c":
        print("")
        print("----REMOVING ITEM!----")
        print("-----CONSUMPTION------")
        islandC_ItemName.remove(dhoaniItemName)
        islandC_ItemAmount.remove(dhoaniItemAmount)
        user_input = input("Remove another item?(yes/no): ").lower()
        print("---------------------------------")
        if user_input == "yes":
            menu_and_travel.consoleMenu()
        else:
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
                menu_and_travel.consoleMenu()
            else:
                exit()

    # Checks if Item Name and Item Amount is valid and removes it.
    elif from_remove == "island d":
        print("")
        print("----REMOVING ITEM!----")
        print("-----CONSUMPTION------")
        islandD_ItemName.remove(dhoaniItemName)
        islandD_ItemAmount.remove(dhoaniItemAmount)
        user_input = input("Remove another item?(yes/no): ").lower()
        print("---------------------------------")
        if user_input == "yes":
            menu_and_travel.consoleMenu()
        else:
            user_input = int(input("Continue (6) or Quit (7): "))
            print("")
            if user_input == 6:
                menu_and_travel.consoleMenu()
            else:
                exit()
    

# This function will search through the lists and print items and their amounts.
# in method to verify and display and index search to display index of elements.
def searchItems():
    print("----SEARCHING ITEMS----")
    print("---------------------------------")
    itemName = input("Item Name: ").lower()
    itemAmount = int(input("Item Amount: "))
    
    # Dhoani
    if ((itemName in dhoaniItemName) and (itemAmount in dhoaniItemAmount)):  
        # Prints Item Name and Item Amount.
        print("")
        print("----ITEM EXISTS!----")
        print("-------DHOANI-------")  
        print("Item Name: " + itemName.upper())
        print("Item Amount: " + str(itemAmount))
        nameIndex = dhoaniItemName.index(itemName)
        amountIndex = dhoaniItemAmount.index(itemAmount)
        print("Item Index: " + str(nameIndex))
        print("Amount Index: " + str(amountIndex))
        
        # Asking user if they wish to continue or quit.
        print("---------------------------------")
        user_input = int(input("Continue (6) or Quit (7): "))
        print("")
        if user_input == 6:
           menu_and_travel.consoleMenu()
        else:
           exit()
    # Island A
    if ((itemName in islandA_ItemName) and (itemAmount in islandA_ItemAmount)):  
        # Prints Item Name and Item Amount.
        print("")
        print("----ITEM EXISTS!----")
        print("-----ISLAND A----")  
        print("Item Name: " + itemName.upper())
        print("Item Amount: " + str(itemAmount))
        nameIndex = dhoaniItemName.index(itemName)
        amountIndex = dhoaniItemAmount.index(itemAmount)
        print("Item Index: " + str(nameIndex))
        print("Amount Index: " + str(amountIndex))
        
        # Asking user if they wish to continue or quit.
        print("---------------------------------")
        user_input = int(input("Continue (6) or Quit (7): "))
        print("")
        if user_input == 6:
           menu_and_travel.consoleMenu()
        else:
           exit()

# This function will deliver items to destinations.
def deliverItems():
    # Calling the menu.
    menu_and_travel.deliverMenu()
    user_input = input("Deliver to island(A, B, C, D)?: ").lower()
    from_to = input("From(Supply Island 01/02)?: ").lower()
    print("---------------------------------")

    # Delivers from Supply island 01 to other islands.
    if from_to in "supply island 01":
        # Checks what destination the user has chosen and displays where it goes.
        if user_input not in ["island a", "island b", "island c", "island d"]:
            # Error Message.
            print("INVALID INPUT")
        # Delivers to Island A.
        elif user_input in "island a":
            islandA_ItemName.append(dhoaniItemName)
            islandA_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 50 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 50KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
            print("---------------------------------")
        # Delivers to Island B.
        elif user_input in "island b":
            islandB_ItemName.append(dhoaniItemName)
            islandB_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 130 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 130KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
            print("---------------------------------")
        # Delivers to Island C.
        elif user_input in "island c":
            islandC_ItemName.append(dhoaniItemName)
            islandC_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 190 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 130KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
            print("---------------------------------")
        # Delivers to Island D.
        elif user_input in "island d":
            islandD_ItemName.append(dhoaniItemName)
            islandD_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 230 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 230KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
            print("---------------------------------")
        # Exits to console menu.
        elif user_input in "quit":
            menu_and_travel.consoleMenu
    
    # Delivers from Supply island 02 to other islands. 
    elif from_to in "supply island 02":
        # Checks what destination the user has chosen and displays where it goes.
        if user_input not in ["island a", "island b", "island c", "island d"]:
            # Error Message.
            print("INVALID INPUT")
        # Delivers to Island A.
        elif user_input in "island a":
            islandA_ItemName.append(dhoaniItemName)
            islandA_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 250 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 250KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
        # Delivers to Island B.
        elif user_input in "island b":
            islandB_ItemName.append(dhoaniItemName)
            islandB_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 170 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 170KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
        # Delivers to Island C.
        elif user_input in "island c":
            islandC_ItemName.append(dhoaniItemName)
            islandC_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 110 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 110KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
        # Delivers to Island D.
        elif user_input in "island d":
            islandD_ItemName.append(dhoaniItemName)
            islandD_ItemAmount.append(dhoaniItemAmount)
            print(menu_and_travel.get_drive() + user_input.upper())
            calc = 70 / 25
            print("Time: " + str(calc) + " HRS")
            print("Distance: 70KM")
            print("---------------------------------")
            print(menu_and_travel.get_stop() + user_input.upper())
        # Exits to console menu.
        elif user_input in "quit":
            menu_and_travel.consoleMenu
    # Exits after displaying error message.
    else:
        print("INVALID INPUT!")
        # Asking user if they wish to continue or quit.
        user_input = int(input("Continue (6) or Quit (7): "))
        if user_input == 6:
            menu_and_travel.consoleMenu()
        else:
            exit()
   
# This function will print all of the lists and their amounts.
def printItems():
    # Dhoani inventory.
    print("")
    print("")
    print("")
    print("Dhoani Inventory")
    print("-----------------------------")
    print("Items: ", *dhoaniItemName)
    print("Amount:", *dhoaniItemAmount)
    print("-----------------------------")

    # Island A inventory.
    print("")
    print("Supply Island A Inventory")
    print("-----------------------------")
    #print("All Items: ", *island_a)
    print("Items: ", islandA_ItemName)
    print("Amount:", islandA_ItemAmount)
    print("-----------------------------")

    # Island B inventory.
    print("")
    print("Supply Island B Inventory")
    print("-----------------------------")
    #print("All Items: ", *island_b)
    print("Items: ", islandB_ItemName)
    print("Amount:", islandB_ItemAmount)
    print("-----------------------------")

    # Island C inventory.
    print("")
    print("Supply Island C Inventory")
    print("-----------------------------")
    #print("All Items: ", *island_c)
    print("Items: ", islandC_ItemName)
    print("Amount:", islandC_ItemAmount)
    print("-----------------------------")

    # Island D Inventory.
    print("")
    print("Supply Island D Inventory")
    print("-----------------------------")
    #print("All Items: ", *island_d)
    print("Items: ", islandD_ItemName)
    print("Amount:", islandD_ItemAmount)
    print("-----------------------------")

    # Asking user if they wish to continue or quit.
    user_input = int(input("Continue (6) or Quit (7): "))
    if user_input == 6:
        menu_and_travel.consoleMenu()
    else:
        exit()
#### ----FUNCTIONS---- ####

# Calling the function globally.
# Displays main console menu.
menu_and_travel.consoleMenu()

# PROGRAM END.
