# 2 Create a class Product with members as pid,pname,price and quantity .Add 
# following methods:  
# d. Constructor (Support both parameterized and parameterless)  
# e. Destructor   
# f. ShowProduct

class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def ShowProduct(self):
        print("Product ID:", self.pid)
        print("product Name:", self.pname)
        print("Product Price:", self.price)
        print("Product Quantity:", self.quantity)

    def __del__(self):
        print("Destructor called")

P1 = Product(10, "Laptop", 70000, 2)
P1.ShowProduct()
del P1

print("**************************************")

P2 = Product(20, "Mobile", 300000, 1)
P2.ShowProduct()
del P2
