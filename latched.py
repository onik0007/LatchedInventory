# Latched Inventory system
# Group 5
# Kino Porteous - 620106882

import os
import fileinput
import time
from getpass import getpass

soldItems = []
    #Main Classes
class Item(object): 
    def __init__(self,name,quantity,price):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getPrice(self):
        return self.price
    def getName(self):
        return self.name
    def getQuantity(self):
        return self.quantity
class Cart(object):
    def __init__(self):
        self.c = dict()

    def addItem(self, item):
        if item.name not in self.c:
            self.c.update({item.name: item})
            return
        for k, v in self.c.get(item.name).items():
            if k == 'name':
                continue
            elif k == 'quantity':
                total_quantity = v.quantity + item.quantity
                if total_quantity:
                    v.quantity = total_quantity
                    continue
                self.remove_item(k)
            else:
                v[k] = item[k]
    def getTotal(self):
        return sum([int(v.price) * int(v.quantity) for _, v in self.c.items()])
    def getNumItems(self):#NOT USED
        return sum([v.quantity for _, v in self.c.items()])
    def removeItem(self, key):#removes the item from the cart's item list
        self.c.pop(key)  
    def cartContents(self):
        return ([v.name for _, v in self.c.items()],[v.price for _, v in self.c.items()],[v.quantity for _, v in self.c.items()])
    def updateSales(self):
        return ([v.name for _, v in self.c.items()],sum([int(v.price) * int(v.quantity) for _, v in self.c.items()])) #Return Total sold items
class Inventory(object):
    def __init__(self):
        self.i = dict()

    def addItem(self, item): #add/update "update not fun"
        if item.name not in self.i:
            self.i.update({item.name: item})
            return
        for k, v in self.i.get(item.name).items():
            if k == 'name':
                continue
            elif k == 'price':
                v.price = item.price
                continue
            elif k == 'quantity':
                total_quantity = v.quantity + item.quantity
                if total_quantity:
                    v.quantity = total_quantity
                    continue
                self.remove_item(k)
            else:
                v[k] = item[k]
    def inventoryContents(self):
        return ([v.name for _, v in self.i.items()],[v.price for _, v in self.i.items()],[v.quantity for _, v in self.i.items()])
    def removeItem(self, key):
        self.i.pop(key)
    def getPrice(self, key):
        if key.name in self.i:
            return key.price
    def searchh(self, key):
        if key.name in self.i:
            #print("Cost: $",key.price," Quantity:",key.quantity)
            return True 
        else:
            print("NO ITEM")
            return False  #a text file to start with current inventory and save to file when system closes. 

class Manager:
    def __init__(self, name,password,email,contactNum):
        self.name = name
        self.password = password
        self.email = email
        self.contactNum = contactNum

    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getContactNum(self):
        return self.contactNum
    def getPassword(self):
        return self.password   

    #Operation Functions  #maybe
#class Sales(object):#maybe

lInventory = Inventory() #Global Inventory 
kart = Cart() #Global cart


def login():
	admin = input("Admin? (Y,N) ")
	if ((admin == "Y") or  (admin == "y")):	
	    user = input("Username: ")
	    passw = getpass('Password: ')

	    f = open("logDetails.txt", "r")
	    for line in f.readlines():
	        us, pw = line.strip().split("|")
	        if (user in us) and (passw in pw):
	            print ("Login successful!")
	            time.sleep(3)
	            os.system('clear')
	            return True
	    print ("Login Failed...")
	    print ("Loading As Employee")
	    return False
	else:
	    return False
##################################################################
##################################################################
def loading():
    for i in range(101):
        print('    ============ ',i,'% ===========')
        os.system('clear')
def mainMenu():
    os.system('clear')
    print('====================================')
    print('=         Latched Inventory        =')
    print(' ==            System            ==')
    print('  ==                            ==')
    print('    ============================')


    print('(1) Add Item to Inventory')
    print('(2) Remove Item from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Inventory')
    print('(5) Inventory Report') 
    print('(6) Sales Report') #items sold for the day, total sales
    print('(7) Add to cart')
    print('(8) Check Out')
    print('(0) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)
def customerMenu():
    os.system('clear')
    print('====================================')
    print('=         Latched Inventory        =')
    print(' ==            System            ==')
    print('  ==                            ==')
    print('    ============================')

    print('(1) Search Inventory')
    print('(2) Add to cart')
    print('(3) Check Out')
    print('(0) Quit')
    CHO = int(input("Enter choice: "))
    menuSelectionC(CHO)
def menuSelectionC(CHO):
    if CHO == 1:
        searchInventoryc()
    elif CHO == 2:
        addToCartc()
    elif CHO == 3:
        checkOutc()
    elif CHO == 0: #save
        #Update File Fun
        salesFile = open('Sales.txt', 'a')
        salesFile.write(str(soldItems))
        salesFile.close()
        exit()
def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 6:
        printSales()
    elif CHOICE == 7:
        addToCart()
    elif CHOICE == 8:
        checkOut()
    elif CHOICE == 0: #save
        #Update File Fun
        salesFile = open('Sales.txt', 'a')
        salesFile.write(str(soldItems))
        salesFile.close()
        exit()
##################################################################
##################################################################
def addInventory():
    InventoryFile = open('Inventory.txt', 'a')
    print("================")
    print("Adding Inventory")
    print("================")
    
    item_description = input("Enter the name of the item: ")
    item_quantity = input("Enter the quantity of the item: ")
    item_price = input("Enter the price of the item: ")
    tempItem = Item(item_description,item_quantity,item_price)
    lInventory.addItem(tempItem)

    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            mainMenu()
    else:
        exit()
def removeInventory():
    print("==================")
    print("Removing Inventory")
    print("==================")
    item_description = input("Enter the item name to remove from inventory: ")
    lInventory.removeItem(item_description)

    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
        mainMenu()
    else:
        exit()
def updateInventory():
    print("==================")
    print("Updating Inventory")
    print("==================")
    
    item_description = input('Enter the item to update: ')
    item_quantity = int(input("Enter the updated quantity: "))
    item_price = int(input("Enter the updated price:"))
    lInventory.removeItem(item_description)
    tempItem = Item(item_description,item_quantity,item_price)
    lInventory.addItem(tempItem)

    print(lInventory.inventoryContents())                  
                
    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            mainMenu()
    else:
        exit() #Bug will not update
def searchInventory():
    print('Searching Inventory')
    print('===================')
    index = 0

    item_description = input('Enter the name of the item:')
    allInventory = lInventory.inventoryContents()
    
    for i in allInventory[0]:
        if i == item_description:
            item_price = allInventory[1][index]
            item_quantity = allInventory[2][index]
            tempItem = Item(item_description,item_price,item_quantity)
            break
        index+=1

    if (lInventory.searchh(tempItem)== True):
        print("Item Found")
        print("Cost: ",item_price)
        print("Quantity: ",item_quantity)
        
    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            mainMenu()
    else:
        exit() 
def searchInventoryc():
    print('Searching Inventory')
    print('===================')
    index = 0

    item_description = input('Enter the name of the item:')
    allInventory = lInventory.inventoryContents()
    
    for i in allInventory[0]:
        if i == item_description:
            item_price = allInventory[1][index]
            item_quantity = allInventory[2][index]
            tempItem = Item(item_description,item_price,item_quantity)
            break
        index+=1

    if (lInventory.searchh(tempItem)== True):
        print("Item Found")
        print("Cost: ",item_price)
        print("Quantity: ",item_quantity)
        
    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            customerMenu()
    else:
        exit() 
def printInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    print(lInventory.inventoryContents())

    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            mainMenu()
    else:
        exit() #inventory contents
def printSales():
    print("Sold items", soldItems[0])
    total = 0
    for i in soldItems:
        total = total+ i[1]
    print("Total sales: $",total)

    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            mainMenu()
    else:
        exit()          
def addToCart(): #-1 from quantity of a specific item after added to cart
    item = []
    index = 0
    print("================")
    print("Adding To Cart")
    print("================")
    
    item_description = input("Enter Item to add to cart: ")
    cart_Quantity = input("Quantity: ")

    allInventory = lInventory.inventoryContents()
    found = False
    for i in allInventory[0]:
        if i == item_description:
            found = True
            item_price = allInventory[1][index]
            print("Cost Per unit: ",item_price)
            tempItem = Item(item_description,item_price ,int(cart_Quantity))
            continue
        index+=1

    
    if (found == True):
        kart.addItem(tempItem)
        print("Added To Cart!")
        print(kart.cartContents())

    else:
        print("OuT Of StoCk!")  

    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            mainMenu()
    else:
        exit()
        #check stock level 
def addToCartc(): #-1 from quantity of a specific item after added to cart
    item = []
    index = 0
    print("================")
    print("Adding To Cart")
    print("================")
    
    item_description = input("Enter Item to add to cart: ")
    cart_Quantity = input("Quantity: ")

    allInventory = lInventory.inventoryContents()
    found = False
    for i in allInventory[0]:
        if i == item_description:
            found = True
            item_price = allInventory[1][index]
            print("Cost Per unit: ",item_price)
            tempItem = Item(item_description,item_price ,int(cart_Quantity))
            continue
        index+=1

    
    if (found == True):
        kart.addItem(tempItem)
        print("Added To Cart!")
        print(kart.cartContents())

    else:
        print("OuT Of StoCk!")  

    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:
            customerMenu()
    else:
        exit()
        #check stock level 
def checkOut():  #add checked out items to a file to store sold items (fun #6)
    
    total = kart.getTotal()
    totalItems = kart.cartContents()
    print("Items in Cart:", totalItems[0],totalItems[1])
    print("Total Cost: : ", total,"Item Unit Cost",totalItems[2])

    print("Total sales:",kart.updateSales()) #updates fun... add to sold item list/ dic
    soldItems.append(kart.updateSales())

    for i in totalItems[0]:
        kart.removeItem(i);
    
    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:  
        mainMenu()
    else:
        exit()
def checkOutc():  #add checked out items to a file to store sold items (fun #6)
    
    total = kart.getTotal()
    totalItems = kart.cartContents()
    print("Items in Cart:", totalItems[0],totalItems[1])
    print("Total Cost: : ", total,"Item Unit Cost",totalItems[2])

    print("Total sales:",kart.updateSales()) #updates fun... add to sold item list/ dic
    soldItems.append(kart.updateSales())

    for i in totalItems[0]:
        kart.removeItem(i);
    
    CHOICE = int(input('Enter 99 to continue or 0 to exit: '))
    if CHOICE == 99:  
        customerMenu()
    else:
        exit()
def inventoryDownload():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory Download:')
    print('-----------------')

    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_price = InventoryFile.readline()

        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        item_price = item_price.rstrip('\n')

        newItem = Item(item_description,item_price,item_quantity)
        lInventory.addItem(newItem)
        item_description = InventoryFile.readline()
    InventoryFile.close() #Downloads the Updated inventory to application from database
##################################################################
##################################################################
if __name__ == '__main__':

    inventoryDownload()

    log = login()
    if log == True :
        mainMenu()
    else:
    	customerMenu()






