# 3 Create a class Shirt  with members as sid,sname,type(formal etc), price and 
# size(small,large etc) .Add following methods:  
 
# g. Constructor (Support both parameterized and parameterless)  
# h. Destructor   
# i. ShowShirt

class Shirt:
    def __init__(self, sid, sname, type, price, size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Shirt Type:", self.type)
        print("Shirt Price:", self.price)
        print("Shirt size:", self.size)

    def __del__(self):
        print("Destructor called")

S1 = Shirt(1, "Polo", "Formal", 2000, "Large")
S1.ShowShirt()
del S1
print("****************************************")

S2 = Shirt(2, "Levis", "Casual", 1500, "Medium")
S2.ShowShirt()
del S2
