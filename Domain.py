import Users

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
