class shop:
    def __init__(self):
        self.grocery_item = dict()
        self.grocery_history = []
        self.apliance_item = dict()
        self.apliance_history = []        

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
        print(self.grocery_history)


    def order_apliance(self):

        self.choice = 0
        self.stop = True
        while self.stop == True:
            self.apliance_item = dict()
            self.apliance_item['name'] = str(input('Item name: '))
            self.apliance_item['quantity'] = int(input('Amount purchased: '))
            self.apliance_item['cost'] = float(input('Price per item: '))
            self.apliance_history.append(self.apliance_item)
            self. choice = str(input('Press c to continue or q to quit : '))
            if self.choice == 'c':
                self.stop = True
            else:
                self.stop = False
        print(self.apliance_history)

    def choice_category(self):
        self.shop_category = ['grocry', 'apliance']
        print("1: {}".format(self.shop_category[0]))
        print("2: {}".format(self.shop_category[1]))
        self.user_choice = int(input())
        if self.user_choice == 1 :
            self.order_grocery()
        elif self.user_choice == 2 :
            self.order_apliance()

sh = shop()
sh.choice_category()