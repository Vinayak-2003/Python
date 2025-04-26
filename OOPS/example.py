class Customers:
        
    def __init__(self, name, contact, email, password):
        self.username = name
        self.__contact = contact
        self.email = email
        self.__password = password
        self.create_user()
    
    def create_user(self):
        
        if self.email not in self._customer:
            self._customer[self.email] = {"username": self.username, "contact": self.__contact, "password": self.__password}
            print(f"User created with username as {self.username}")
            self.increase_customer()
        else:
            print(f"Welcome again {self.username}")
            
    @classmethod
    def increase_customer(cls):
        cls._no_of_customers += 1
        

class Products(Customers):
    
    monitor = 20
    keyborad = 15
    CPU = 10
    mouse = 30
    speakers = 20
    camera = 15
    
    monitor_cost = 10000
    keyborad_cost = 3000
    CPU_cost = 9000
    mouse_cost = 300
    speakers_cost = 2500
    camera_cost = 1500
    
    def __init__(self, name, contact, email, password):
        super().__init__(name, contact, email, password)
        self.cart = {}
        
    @staticmethod
    def show_products():
        print("""
                 1. Monitors
                 2. Keyboard
                 3. CPU
                 4. Mouse
                 5. Speaker
                 6. Camera
            """)
    
    @staticmethod
    def other_details_for_products():
        print("""
                 Monitor:  size - 24inch, 27inch, 32inch, brand - LG, Samsung
                 Keyboard:  size - small, large brand - Logitech
                 CPU:  RAM - 8GB, 16GB
                 Mouse:  feature - normal, silent, wired, non-wired brand - Lenovo, LG, HP
                 Speaker:  size - small, large brand - JBL, samsung, SONY
                 Camera:  pixel - 5px, 8px, 10px brand - Samsung, SONY
            """)
    
    @classmethod
    def _total_products(cls):
        count = cls.monitor+cls.keyborad+cls.CPU+cls.mouse+cls.speakers+cls.camera
        print(f"Total products in the inventory are {count}")
    
    @classmethod
    def _total_products_costs(cls):
        total_cost = (cls.monitor*cls.monitor_cost)+(cls.keyborad*cls.keyborad_cost)+(cls.CPU*cls.CPU_cost)+(cls.mouse*cls.mouse_cost)+(cls.speakers*cls.speakers_cost)+(cls.camera*cls.camera_cost)
        print(f"Total cost of the products in the inventory are {total_cost}")


class ShoppingCart(Products):
    _no_of_customers = 0
    _customer = {}

    def add_to_cart(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1
        print(f"{item} added in the cart")
    
    def remove_from_cart(self, item):
        if item in self.cart:
            if self.cart[item] >= 1:
                self.cart[item] -= 1
                print(f"{item} removed from the cart")
        else:
            print(f"{item} is not in cart")
            
    def total_amount(self):
        amount = 0
        for item,count in self.cart.items():
            if item == "monitor" or item == "Monitor":
                amount += count*self.monitor_cost
                Products.monitor -= count
            elif item == "keyboard" or item == "Keyboard":
                amount += count*self.keyborad_cost
                Products.keyborad -= count
            elif item == "CPU":
                amount += count*self.CPU_cost
                Products.CPU -= count
            elif item == "mouse" or item == "Mouse":
                amount += count*self.mouse_cost
                Products.mouse -= count
            elif item == "speaker" or item == "Speaker":
                amount += count*self.speakers_cost
                Products.speakers -= count
            elif item == "camera" or item == "Camera":
                amount += count*self.camera_cost
                Products.camera -= count
            else:
                print("Item does not exist please re-enter the correct product")
        print(f"Total amount of the cart is {amount}")
    
    def show_cart(self):
        for item,count in self.cart.items():
            print(f"{count} {item}")


def create_customer():
    name, contact, email, password = input("Enter name, contact, email, password: ").split()
    new_customer = ShoppingCart(name, contact, email, password)
    new_customer.show_products()
    new_customer.other_details_for_products()
    input_operation = ""
    while input_operation != "4":
        input_operation = input("""
                                Select operation: 
                                1. add item
                                2. remove item
                                3. show cart
                                4. checkout for payment
                                """)
        if input_operation == "1":
            item_to_add = input("Enter product to add: ")
            new_customer.add_to_cart(item_to_add)
        elif input_operation == "2":
            item_to_remove = input("Enter product to remove: ")
            new_customer.remove_from_cart(item_to_remove)
        elif input_operation == "3":
            new_customer.show_cart()
        elif input_operation == "4":
            break
        else:
            print("Operation does not exist, re-enter the operation number")
    new_customer.total_amount()
    
    
def create_owner():
    owner = ShoppingCart("complex.owner", "83827487", "complex.owner@gmail.com", "complex.owner")
    input_operation = ""
    while input_operation != "5":
        input_operation = input("""
                                Select operation: 
                                1. Total number of customers
                                2. See all customer information
                                3. Total products in Inventory
                                4. Total cost of Inventory
                                5. Exit
                                """)
        if input_operation == "1":
            print(f"Total number of customers are {owner._no_of_customers-1}")
        elif input_operation == "2":
            for key,info in owner._customer.items():
                print(f"Email: {key} - {info}")
        elif input_operation == "3":
            owner._total_products()
        elif input_operation == "4":
            owner._total_products_costs()
        elif input_operation == "5":
            break
        else:
            print("Operation does not exist, re-enter the operation number")


input_operation = ""
while input_operation != "3":
    input_operation = input("""
                            Select operation: 
                            1. Create customer
                            2. Welcome owner
                            3. Exit
                            """)
    if input_operation == "1":
        create_customer()
    elif input_operation == "2":
        create_owner()
    elif input_operation == "3":
        break
    else:
        print("Operation does not exist, re-enter the operation number")