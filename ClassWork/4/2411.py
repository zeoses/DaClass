#!/usr/bin/env python3

# # Format
# s = 'Hello'
# s1 = ' world'

# print('{}{}.'.format(s,s1))

# # file
# # f = open('3.txt','x')
# # (f.write('ds'))

# # f.close()

# # with
# with open('2.txt', 'w')as f:
#     f.write('2')
#     # data = f.read()
#     # for l in f:
#     #     print(l,end='')
#     # a = list(f)
#     # print(*a, end= '\n')
#     # data = f.read()
#     # print(data)


# import sys

# with open(sys.argv[1], 'r') as f:
#     print(*list(f))
# try:
#     adad = int(input())
#     print(adad+1)
# except ValueError as E:
#     print(E)
# finally:
#     print('s')
# esm = input()
# if esm == 'Ali':
#     print('ok')
# else:
#     raise NameError('Faghat Ali')

def Scop_test():
    def one():
        text = '1'
    def two():
        nonlocal text
        text = '2'
    def three():
        global text 
        text = '3'

    text = 'test'
    one()
    print(text)
    two()
    print(text)
    three()
    print(text)

Scop_test()
print(text)