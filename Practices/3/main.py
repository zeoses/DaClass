from Modules import sumMa,Scaler, Transpose
import os

Amatrix=list()
Bmatrix=list()
mainMenulst= ['1 - Add/Change matrixs','2 - Sum',
 '3 - Scaler','4 - Transpose', '5 - Exit']


def recurringCommands(Message=''):
    os.system('clear')
    
    print(Message)

row = column = 0
recurringCommands()

while(True):
    try:

        print(*mainMenulst, sep='\n')
        command = int(input()) - 1
        
        if command == 0:
            recurringCommands(mainMenulst[command])
            column = int(input('Enter column of Matrix:'))
            row = int(input('Enter Row of Matrix:'))
            print('Matrix1:')
            Amatrix = ([list(map(int,input().split())) for j in range(row)])
            print('Matrix2:')
            Bmatrix = ([list(map(int,input().split())) for j in range(row)])
            print('-----')
            print(*Amatrix,end='\n')
            print('-----')
            print(*Bmatrix,end='\n')
            input()

        elif len(Amatrix)>0:
            if command == 1:
                recurringCommands(mainMenulst[command])
                print(*Amatrix,end='\n')
                print('-----')
                print(*Bmatrix,end='\n')
                print('-----')
                print('Result : ')
                result = sumMa.sumMatrix(row, column, Amatrix, Bmatrix)
                print(*result)
                input()
            
            elif command == 2:
                recurringCommands(mainMenulst[command])
                num = int(input('Please Eneter a number:'))
                result = Scaler.ScalerMatrix(row,column,Amatrix,num)
                result2 = Scaler.ScalerMatrix(row,column,Bmatrix,num)
                print('matrix 1 : \n',*Amatrix,end='\n')
                print('-----')
                print('result : \n',*result, end='\n')
                print('-----')
                print('matrix 2 : \n',*Bmatrix,end='\n')
                print('-----')
                print('result : \n',*result2, end='\n')

                input()

            elif command == 3:
                recurringCommands(mainMenulst[command])
                result = Transpose.TransposeMatrix(row,column,Amatrix)
                print(*result, end='\n')
                input()

            elif command == 4:
                recurringCommands(mainMenulst[command])
                break

            
        else:
            recurringCommands()
            print('Please Enter a number in 1 to 5')
            input()
        recurringCommands()

    except  (ValueError, NameError):
        recurringCommands('Please be careful in entering information. ')
    


recurringCommands()
