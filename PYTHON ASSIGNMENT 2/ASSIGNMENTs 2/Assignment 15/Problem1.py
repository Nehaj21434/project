# assinment Q 1
# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Book Price:", self.price)
        print("Book Author:", self.author)

    def __del__(self):
        print("Destructor called")

B1 = Book(101, "Python programming", 500, "John Doe")
B1.ShowBook()
del B1
print("***************************************")

B2 = Book(111, "java programming", 800, "Jane")
B2.ShowBook()
