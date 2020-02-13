class player :
    def __init__(self, race):
       self.race = race
       self.HP = 100
       self.AP = 10
       self.DP = 10
       self.MP = 5
       if race == 'Elf':
           self.MP = 15 
    

myplayer = player()

print(myplayer.HP)
# print(dir(myplayer))
myplayer.HP+= 10 
print(myplayer.HP)


