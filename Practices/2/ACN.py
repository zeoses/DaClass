import os
import pandas as pd

mainMenulst= ['1 - Set Student and Course Count',
 '2 - GPA Students','3 - Display All Score','4 - Edit Score' , '5 - Course Report', '6 - Exit']


def recurringCommands(Message=''):
    os.system('clear')
    print(Message)


recurringCommands()
studentCount = 0
CourseCount = 0

gradeList= list()

while(True):
    try:
        print(*mainMenulst, sep='\n')
        command = int(input())
        
        if command == 1:
            recurringCommands(mainMenulst[command -1])
            studentCount = int(input('Student Cont : '))
            CourseCount = int(input('Course Cout : '))
            gradeList = list()
            print('Please separate the grades for each lesson.')
            for i in range(studentCount):
                print('Studet '+str(i+1) +' : ', end='')
                gradeList.append(list(map(float,input().split())))
                
            
            print('Information entered successfully.')
            input()

        elif command == 2:
            recurringCommands(mainMenulst[command -1])
            for i in range(studentCount):
                avg = sum(gradeList[i])/len(gradeList[i])
                print('Studet '+ str(i+1) +' : '+ str(avg))
            input()

        elif command == 3:
            recurringCommands(mainMenulst[command -1])
            for i in range(studentCount):
                print('Studet '+ str(i+1) +' : ', end='')
                print(*gradeList[i], sep=' ' )
            input()

        elif command == 4:
            recurringCommands(mainMenulst[command -1])
            stid = int(input('Student ID : '))
            print('Old Score : ', end='')
            print(*gradeList[i-1], sep=' ' )
            print('New Score : ', end='')
            gradeList[i-1] = list(map(float, input().split()))
            print(gradeList[i-1])
            input()

        elif command == 5:
            recurringCommands(mainMenulst[command -1])
            df = pd.DataFrame(gradeList) 
            print('\t\tmin  \tmax \tave')
            for i in range(CourseCount):
                print('Course '+ str(i+1) +' : \t'+ str(df[:][i].min())+ '\t' + str(df[:][i].max())+'\t'+ str(df[:][i].mean()))
            input()


        elif command == 6:
            break


        recurringCommands()


    except (ValueError, NameError):
        recurringCommands()
        print('Be careful in entering information')
    

    
recurringCommands()

