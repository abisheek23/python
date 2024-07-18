class sample:
    def __init__(self,name,age):
        print("sample class display method")
        print(name,age)
    def s1(self):
        print("sample class s1 method")

class demo(sample):
    def __init__(self,name,age):
        print(name,age)
        super().__init__(name,age)
        print("demo class display method")
    def d1(self):
        print("demo class d1 method")
obj=demo("akhil",34)
