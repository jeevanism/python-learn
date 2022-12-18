import sys

class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age= age
        self.sound = sound
        

        
# how to return as JSON 

class Dog(Animal):
    def getName(self):
        return self.name
        
    def getAge(self):
        return self.age
        
    def getSound(self):
        return self.sound


        
    


# class Dog(Animal):
#     def getName(self):
#         print("Hello I am " + self.name)
#         return self
        
#     def getAge(self):
#         print("I am " + str(self.age) + " old")
#         return self
        
#     def getSound(self):
#         print("I do " + self.sound)
#         return self
        
    
        
        
    