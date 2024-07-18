class sample:
    def display(self):
        print("sample class display method")
    def s1(self):
        print("sample class s1 method")

class demo(sample):
    def display(self):
        super().display()
        print("demo class display method")
    def d1(self):
        print("demo class d1 method")
obj=demo()
obj.display()