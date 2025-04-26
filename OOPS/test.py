class A:
    
    def __init__(self):
        self.num = 100
        
    def display1(self, num):
        print("class A: ", num)
        
class B(A):
    
    def display2(self, num):
        print("class B: ", self.num)
        
obj = B()
obj.display1(200)