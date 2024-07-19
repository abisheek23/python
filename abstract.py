from abc import ABC,abstractmethod
class animel(ABC):
    @abstractmethod
    def make_sound(self):
        print("sound")
class bird(animel):
    def fly(self):
        print("fly")
    def make_sound(self):
        print("bird sound")
class cat (animel):
    def run(self):
        print("run")
    def make_sound(self):
        print("run")
b1=bird()
b1.fly()
b1.make_sound()
print('cat')
c=cat()
c.run()