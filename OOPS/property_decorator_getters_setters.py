class celsius:
    def __init__(self, temp=0):
        # self.set_temp(temp)
        self.temp = temp
        
    def to_Fehrenheit(self):
        return (self.temp * 1.8) + 32


    def get_temp(self):
        print("Gettingg valluee....")
        return self._temp
    
    
    def set_temp(self, val):
        print("Settingg valluee...")
        if val<-273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temp = val
        
    temp = property(get_temp, set_temp)



# creating a new object   
# human = celsius()

# setting the temp
# human.temp = 37

# print(human.temp)
# print(human.to_Fehrenheit())
# print(human.__dict__)


# --------------------------------------------------- #
# human = celsius(37)
# print(human.get_temp())
# print(human.to_Fehrenheit())

# human.set_temp(-300)
# print(human.to_Fehrenheit())


# --------------------------------------------------- #
human = celsius(37)
print(human.temp)
print(human.to_Fehrenheit())
# human.temp = -300