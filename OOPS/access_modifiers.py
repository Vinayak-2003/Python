class student:
    
    # protected data members
    _name = None
    # private data member
    __roll = None
    __branch = None
    
    def __init__(self, name, roll, branch):
        self._name = name
        self.__roll = roll
        self.__branch = branch
        
    # protected member function
    def _displayRollAndBranch(self):
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)
        

class child(student):
    # constructor
    def __init__(self, name, roll, branch):
        student.__init__(self, name, roll, branch)
        
    def displayDetails(self):
        print("Name: ", self._name)
        self._displayRollAndBranch()



obj = child("R2J", 61253, "IT")
obj.displayDetails()