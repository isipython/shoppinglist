class shop:
    def __init__(self):
        self.grocery_item = dict()
        self.grocery_history = []

    def order(self):

        self.choice = 0
        self.stop = True
        while self.stop == True:
            self.current_item = dict()
            self.current_item['name'] = str(input('Item name: '))
            self.current_item['quantity'] = int(input('Amount purchased: '))
            self.current_item['cost'] = float(input('Price per item: '))
            self.grocery_history.append(self.current_item)
            self. choice = str(input('Press c to continue or q to quit : '))
            if self.choice == 'c':
                self.stop = True
            else:
                self.stop = False
        print(self.grocery_history)

    @property
    def ordeer(self):
        return self.grocery_history 

sh = shop()
sh.order()