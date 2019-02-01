class Item:
    # attribute

    #constructor
    def __init__(self,lst):
        self.nam = lst
        self.grocery_item = dict()
        self.grocery_history = []
    
    # properties
    @property
    def name(self):
        return self.nam
class ss:

        #constructor
    def __init__(self):
        self.grocery_item = dict()
        self.grocery_history = []

    def order_grocery(self):

        self.choice = 0
        self.stop = True
        while self.stop == True:
            self.grocery_item = dict()
            self.grocery_item['name'] = str(input('Item name: '))
            self.grocery_item['quantity'] = float(input('Amount purchased: '))
            self.grocery_item['cost'] = float(input('Price per item: '))
            self.grocery_history.append(self.grocery_item)
            self. choice = str(input('Press c to continue or q to quit : '))
            if self.choice == 'c':
                self.stop = True
            else:
                self.stop = False
        return self.grocery_history
s= ss()
l = s.order_grocery()
it = Item(l)
print(str(it.name))
st = str(it.name)
print(st)


import pickle

with open('shoplist.txt', 'ab') as fp:
    pickle.dump(st, fp)