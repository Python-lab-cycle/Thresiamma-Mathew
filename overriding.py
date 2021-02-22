class publisher:
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("name:",self.pname)
class book(publisher):
    def __init__(self,pname,bname,author): 
        self.pname=pname
        self.bname=bname
        self.author=author
    def display(self): 
        print("pname:",self.pname)
        print("bname:",self.bname)
        print("author:",self.author)
class python(book):
    def __init__(self,pname,bname,author,page,price):
        self.pname=pname
        self.bname=bname
        self.author=author
        self.page=page
        self.price=price
    def display(self):    
        print("pname:",self.pname)
        print("bname:",self.bname)
        print("author:",self.author)
        print("page:",self.page)
        print("price:",self.price)
n=input("enter publisher")
b=input("enter book")
a=input("enter author")
p=int(input("enter page"))
pr=int(input("enter price"))
obj=python(n,b,a,p,pr)
obj.display()
