# class player :
#     def __init__(self, race):
#         self.race = race
#         self.level = 1

#         if self.race == 'Human':
#             self.HP = 110
#         else:
#             self.HP = 100
#     def levelup(self):
#         self.level +=1
#         self.HP +=10

#     def __str__(self):
#         return str(self.race) +' HP : ' + str(self.HP)

# class Human(player):
#     def __init__(self):
#         #player.__init__(self, 'Human')
#         super().__init__('Human')
# class Elf(player):
#     def levelup(self):
#         self.level +=1
#         self.HP +=15

# class SuperHuman(Human, Elf):
#     def __str__(self):
#         return 'Super ' +str(self.race) +' HP : ' + str(self.HP)


# a =SuperHuman()
# print(a)
# a.levelup()
# print(a)


# # Structure
# class Student():
#     pass

# Student.name = 'ali'

# ali = Human()
# ali.levelup()
# print(ali)

# vali = player('Elf')
# print(vali)
# s ='slam'
# m = iter(s)
# print(next(m))
# print(next(m))
# print(next(m))

# # for c in m:
# #     print(c)

# a = [1, 2]
# b= iter(a)
# print(next(b))

# iter Class

class mylist():
    def __init__(self, data):
        self.data = data
        self.index = -1
    
    def __iter__(self):
        pass

    def __next__(self):
        self.index +=1
        if self.index >= len(self.data):
            raise StopIteration
        else:
            return self.data[self.index]



def main():

    c= 'as'

    b = mylist(c)

    # for i in b:
    #     print(i)
    print(next(b))
    print(next(b))
   


if __name__ == "__main__":
    main()