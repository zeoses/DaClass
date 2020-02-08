
lst = [1, 3, 2, 12, 9, 9]
lstt = [1, 3, 2, 12, 9, 9]

# append : insert a item to list
lst.append(11)

# extend : merge two list {list1 list2}
lst2 = [40, 60]
lst.extend(lst2)

# remove : remove a item 
lst.remove(1)

# clear : remove all item in list
lst3 = [3]
lst3.clear()

# index : reternt index a pramert(return first index of item)
print(lst.index(3))

# count : return Repeat of item
print(lst.count(9))

# sort 
print(lst)
lst.sort()
print(lst)

# reverse 
lst.reverse()
print(lst)

# pop : remove last item of list
print(lstt.pop())

# popleft
# print(lstt.popleft())

print(*lst)
print(*lst3)


# list to list
lst4 = [[1, 2], ['f', 'w'], [':)', '*']]
print(lst4[2][1])

# string 
m = 'I love python'
print(m[4])

# Set : 
myset = {1, 3, 2}
myset.add(2)
print(myset)

# dict
myDict= {}
myDict = {'a':1 ,'c':3 ,'b':2}
print(myDict['a'])
print(sorted(myDict))
print(list(myDict))
print('a' in myDict)

for item,key in myDict.items():
    print(item,key)

## insert to dct
myDict['e'] = 4

## get : return Value if exies else none
print(myDict.get('s'))

# 