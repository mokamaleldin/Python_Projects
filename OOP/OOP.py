import random

###car
class Car:
    def __init__(self,color,speed,oil): 
        self.color=color 
        self.speed=speed
        self.__oil=oil #Private
        
    def drive(self):
        print(f"the {self.color} car work with {self.speed}")
        print(f"the oil is {self.__oil}")
    
    def stop(self):
        print("Stop the car")




###coin
class Coin:
    def __init__(self):
        self.sideup="Heads"
    
    def toss(self):
        if random.randint(0,1) ==0:
            self.sideup="Heads"
        else:
            self.sideup="Tails"

    def getSideup(self):
        return self.sideup




###person
class person:
    def __init__(self,name):
        self.__name = name 

    # Setters
    def setName(self,newName):
        self.__name=newName

    #Getters
    def getName(self):
        print( self.__name )

