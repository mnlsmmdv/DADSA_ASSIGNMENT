"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: DADSA                            
Date: 10/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Assignment
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

# PROGRAM END.
