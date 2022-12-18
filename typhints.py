import sys

class Vehicle:
    CURRENT_YEAR = 2022
    
    def getDetails(self, type: str, name: str, make: int):
    
     typeofVeh = type.capitalize()
     nameofVeh = name
     makeofVeh = self.CURRENT_YEAR - make
     
      
     
     details ={
         "type" : typeofVeh,
         "name": nameofVeh,
         "make" : makeofVeh
         
     }
         
         
         
   
     print(details)
     
    
 
 
 
bike = Vehicle()

bike.getDetails("bike","vikrant",2016)
bike.getDetails("bike","pulsar",2014)


