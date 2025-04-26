class Customers:
        
    def __init__(self, name, contact, email, password):
        self.username = name
        self.__contact = contact
        self.email = email
        self.__password = password
        self.create_user()
    
    def create_user(self):
        
        if self.email not in self.customer:
            self.customer[self.email] = [self.username, self.__contact, self.__password]
            print(f"User created with username as {self.username}")
            self.increase_customer()
        else:
            print(f"Welcome again {self.username}")
            
    @classmethod
    def increase_customer(cls):
        cls.no_of_customers += 1
            

class Inventory:
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
    
    def total_products(self):
        count = self.monitor+self.keyborad+self.CPU+self.mouse+self.speakers+self.camera
        print(f"Total products in the inventory are {count}")
    
    def __total_products_costs(self):
        total_cost = (self.monitor*self.monitor_cost)+(self.keyborad*self.keyborad_cost)+(self.CPU*self.CPU_cost)+(self.mouse*self.mouse_cost)+(self.speakers*self.speakers_cost)+(self.camera*self.camera_cost)
        print(f"Total cost of the products in the inventory are {total_cost}")
        
    # @staticmethod
    # def hello():
    #     print("HELLOO")


class Products(Customers):
    
    @staticmethod
    def show_products():
        print("""
                 1. Monitors
                 2. Keyboard
                 3. CPU
                 4. Mouse
                 5. Speakers
                 6. Camera
            """)
    
    @staticmethod
    def other_details_for_products():
        print("""
                 Monitor:  size - 24inch, 27inch, 32inch, brand - LG, Samsung
                 Keyboard:  size - small, large brand - Logitech
                 CPU:  RAM - 8GB, 16GB
                 Mouse:  feature - normal, silent, wired, non-wired brand - Lenovo, LG, HP
                 Speakers:  size - small, large brand - JBL, samsung, SONY
                 Camera:  pixel - 5px, 8px, 10px brand - Samsung, SONY
            """)


class ShoppingCart(Products):
    no_of_customers = 0
    customer = {}
    def __init__(self, name, contact, email, password):
        super().__init__(name, contact, email, password)
        self.cart = {}
        
    
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
                amount += count*Inventory.monitor_cost
                Inventory.monitor -= count
            elif item == "keyboard" or item == "Keyboard":
                amount += count*Inventory.keyborad_cost
                Inventory.keyborad -= count
            elif item == "CPU":
                amount += count*Inventory.CPU_cost
                Inventory.CPU -= count
            elif item == "mouse" or item == "Mouse":
                amount += count*Inventory.mouse_cost
                Inventory.mouse -= count
            elif item == "speakers" or item == "Speakers":
                amount += count*Inventory.speakers_cost
                Inventory.speakers -= count
            elif item == "camera" or item == "Camera":
                amount += count*Inventory.camera_cost
                Inventory.camera -= count
            else:
                print("Item does not exist please re-enter the correct product")
        print(f"Total amount of the cart is {amount}")
    
    def show_cart(self):
        for item,count in self.cart.items():
            print(f"{count} {item}")



customer_1 = ShoppingCart("vinayak", "927383863", "vinayak@gmail.com", "hduwhd")
customer_2 = ShoppingCart("vinaya", "927383863", "vinaya@gmail.com", "hduwhd")
customer_1.show_products()
customer_1.other_details_for_products()
customer_1.add_to_cart("monitor")
customer_1.add_to_cart("monitor")
customer_1.show_cart()
customer_1.total_amount()
inventory = Inventory()
inventory.total_products()
# customer_1.hello()
customer_2.show_products()
customer_2.other_details_for_products()
customer_2.add_to_cart("monitor")
customer_2.add_to_cart("CPU")
customer_2.add_to_cart("speakers")
customer_2.add_to_cart("mouse")
customer_2.show_cart()
customer_2.total_amount()
inventory.total_products()
print(ShoppingCart.no_of_customers)