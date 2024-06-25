class car:
    __maxspeed = 0
    __name = " "
    def __init__(self):
        # self.__updateSoftware()
        self.__maxspeed = 200
        self.__name = "lambo"
        
    def drive(self):
        print("driving")
        print(self.__maxspeed)
        print(self.__name)

    # def __updateSoftware(self):
    #     print("Updating the software")
    
    def setspeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
        

blackCar = car()
blackCar.drive()
blackCar.setspeed(100)
blackCar.__name = "BMW"                 #cannot be changed from outside
blackCar.drive()
# blackCar.__updateSoftware()           #cannot be accessed from outside
# blackCar._car__updateSoftware()