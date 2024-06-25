from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class laptop(computer):
    def process(self):
        print("RUNNINGGG")


class programmer:
    def work(self, com):
        print("SOLVEE BUGSS")
        com.process()
    
# com = computer()        #can't  access abstarct class
# com.process()

lap1 = laptop()
# lap1.process()

prog1 = programmer()
prog1.work(lap1)