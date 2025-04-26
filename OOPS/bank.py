class account: 
    __counter = 1                           # class variable
      
    def __init__(self, total_balance, name):
        # instance variable
        self.sno = account.__counter
        self.balance = total_balance
        self.name = name
        
        account.__counter += 1
        print(f"Account created for user {self.name} in the Bank")
    
    @staticmethod
    def get_counter():
        return account.__counter
    
    @staticmethod
    def set_counter(new):
        account.__counter = new
        
    def add_money(self, add_amount):
        self.balance += add_amount
        print(f"{self.name} has added {add_amount}. New balance is {self.balance}")
        
    def transfer_money(self, pay_amount, too, int_rate):
        amount = pay_amount + (pay_amount * int_rate)
        self.balance -= amount
        too.balance += amount
        print(f"{self.name} has transfered {amount}.New balance is {too.balance} and {self.name} balance is {self.balance}")


class savings_account(account):
    def saving_transfer_money(self, pay_amount, too):
        if pay_amount <= self.balance:
            if pay_amount <= 500:
                return super().transfer_money(pay_amount, too, 0.003)
            raise Exception("Transfer amount from savings amount must be less than Rs.500")
        else:
            raise Exception("INSUFFICIENT BALANCE")


class current_account(account):    
    def current_transfer_money(self, pay_amount, too):
        if pay_amount <= self.balance:
            return super().transfer_money(pay_amount, too, 0.001)
        else:
            raise Exception("INSUFFICIENT BALANCE")
    
    
# ---------------------------------------------------------------------
a = savings_account(4000, 'A')
b = savings_account(5000, 'B')
c = current_account(6000, 'C')
d = current_account(7000, 'D')


a.add_money(1000)
b.add_money(1000)
c.add_money(1000)
d.add_money(1000)

c.__counter = "dhwud"
print(c.sno)

c.set_counter("djhaj")
print(c.sno)

# account.set_counter("jssjsj", "jdsj")
account.get_counter()

# a.saving_transfer_money(700, d)
# b.saving_transfer_money(100, c)
# c.current_transfer_money(100, a)
# d.current_transfer_money(100, b)