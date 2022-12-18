import sys
import json
#to import a particular class from another file 
from animal import Dog # Dog is a child class in the animal.py file



# class Dog:
#     def __init__(self, sound):
#         self.sound= sound
        

#     def makeSound(self):
#         print ("Hello I am appu and I " + self.sound)
        
        
# appu = Dog('Bow Bow ')
# appu.makeSound()


appu = Dog("Appu", 15, "Bow Bow")
#appu.getName().getAge().getSound()
#pack into python dictionary 
appuDetails = {
    'name' :appu.getName(),
    'age' : appu.getAge(),
    'sound':appu.getSound()
}
print(appuDetails['name'])

#convert into json 
jsonAppuDetails = json.dumps(appuDetails)

# print (type(jsonAppuDetails)) - type of json in python is string

# for key,value  in jsonAppuDetails.items():
#     print (key, value)
# above will throw error because the python items() cannot handle handle json, need to parse into string using json.lods(jsonfile)

strAppuDetails = json.loads(jsonAppuDetails)
for key,value  in strAppuDetails.items():
    print (key, value)
    
    
# python array / list 

listAppu = [
      appu.getName(),
      appu.getAge(),
      appu.getSound()
]
    
listAppu.append("Poothotta")
listAppu.reverse
print (listAppu)
 

