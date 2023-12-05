class shoppinglist():
    def __init__(self,food="",amount=0):
        self.food = food
        self.amount = amount
        self.std_price = 0
        self.__pricelist()
        self.cost_orderedfood = self.cost_ordered_food()

    def __pricelist(self):
        if self.food == "Dry Cured Iberian Ham":
            self.std_price = 177.80

        elif self.food == "Wagyu Steaks":
            self.std_price = 450.00
        
        elif self.food == "Matsutake Mushrooms":
            self.std_price = 272.00
        
        elif self.food == "Kopi Luwak Coffee":
            self.std_price = 306.50
        
        elif self.food == "Moose Cheese":
            self.std_price = 487.20
        
        elif self.food == "White Truffles":
            self.std_price = 3600.00
        
        elif self.food == "Blue Fin Tuna":
            self.std_price = 3603.00
        
        elif self.food == "Le Bonnotte Potatoes":
            self.std_price = 270.81

        else:
            self.std_price = 0

    def cost_ordered_food(self):
        return self.amount * self.std_price
    
    def __str__(self):
        return f"{self.food}\n{self.amount}\n{self.std_price}"
    

        