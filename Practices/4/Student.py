class Student :
    def __init__(self,id, name, family, grade, math, scince, alghebra, computer):
        
        self.id = id
        self.name = name
        self.family = family
        self.grade = grade
        self.math = math
        self.scince = scince
        self.alghebra = alghebra
        self.computer = computer

    def AverageScore(self):
        res = (self.math + self.scince + self.alghebra + self.computer)/4
        return res
    