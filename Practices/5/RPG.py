import time

class Plant():
    def __init__(self):
        self.level = 1
        self.fertilizer = 1
        self.maxlevel = 42

    def levelUp(self):
        if self.level <  self.maxlevel:
            self.level +=1
     
class Flower(Plant):

    def __init__(self):
        super().__init__()
        self.cost = 1
        
        
    def proLevelUp(self):
        if self.level <  self.maxlevel:
            self.level += 4

        if self.level <  self.maxlevel:
            self.level = self.maxlevel
    
    def sell():
        if 9 < self.level <= 14:
            return 2.5

        elif 14 < self.level <= 17:
            return 4

        elif 17 < self.level <= 23:
            return 5

        elif 23 < self.level <= 26:
            return 5.5

        elif 26 < self.level <= 30:
            return 6.25

        elif 30 < self.level <= 40:
            return 7

        elif self.level > 40:
            return 12

class Baobab(Plant):
    def __init__(self):
        super().__init__()
        self.cost = 3

    def proLevelUp(self):
        if self.level <  self.maxlevel:
            self.level += 2
        
        if self.level <  self.maxlevel:
            self.level = self.maxlevel
    
    def sell():

        if 9 < self.level <= 14:
            return 1

        elif 14 < self.level <= 17:
            return 3

        elif 17 < self.level <= 23:
            return 6

        elif 23 < self.level <= 26:
            return 8

        elif 26 < self.level <= 30:
            return 10

        elif 30 < self.level <= 40:
            return 12

        elif self.level > 40:
            return 20

class Fox():
    def __init__(self):
        self.cost = 5
        self.HP = 10 
        self.level = 1 
        self.DP = 3
        self.exirCost =3
    
    def levelUp(self):
        self.level += 1
        self.DP += 0.5 * self.level
        self.HP += 3 * self.level
    
    def ‌‌BuyElixir():
        self.HP += 3
        self.DP +=1
        

class Snak():
    def __init__(self, type):
        
        if type == 1:
            self.FP = 2
        elif type == 2:
            self.FP = 4
        elif type == 3:
            self.FP = 8

        self.HP = 8

        self.level = 1 
    
    def fight(self, fox):
        self.HP -= fox.DP
        fox.HP -= self.FP
    
class Character():
    def __init__(self, charName, plantName,):
        self.charName = charName
        self.plantName = plantName
        self.coin = 10
        self.level = 1
        self.XP = 0
        self.listOfFlower = list()
        self.listOfBaobab = list()
        self.listOfFox = list()

    def LevelUp(self):
        if self.XP >= self.level * 10:
            self.level +=1
            self.XP -= self.level * 10
    
    def Buy(self, type, obj):
        
        if type == 1:
            self.listOfFlower.appnd(obj)
            self.coin -= obj.cost
            self.XP += obj.cost

        elif type == 2:
            self.listOfBaobab.appnd(obj)
            self.coin -= obj.cost
            self.XP += obj.cost

        elif type == 3:
            self.listOfFox.appnd(obj)
            self.coin -= obj.cost
            self.XP += obj.cost
        


    def Sell(self, type):
        if type == 1:
            if len(self.listOfFlower)> 1:
                flower = self.listOfFlower.pop(0)
                self.coin += flower.sell()
                self.XP += flower.level

        if type == 2:
            if len(self.listOfBaobab)> 1:
                baobab = self.listOfBaobab.pop(0)
                self.coin += baobab.sell()
                self.XP += baobab.level
                
        

    def Buyfertilizer(type):
        if type ==1:
            if len(listOfFlower) > 1:
                for i in listOfFlower:
                    i.proLevelUp()
                self.XP += 1

        if type ==2:
            if len(listOfBaobab) > 1:
                for i in listOfBaobab:
                    i.proLevelUp()
                self.XP += 2
                
# def main():
#     CharName = input('Please Enter Your Name :')
#     plantName = input('Please Enter Your Planet Name :')
#     Character = Character(charName,plantName)
