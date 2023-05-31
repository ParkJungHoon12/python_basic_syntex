from datetime import datetime


class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def register(self):
        self.myinfo = self.name + " " + str(self.age) + " " + self.gender + " " + self.email + " " + str(datetime.now())


p1 = Person("junghun", 23, "Male", "junghun20608@nate.com")
p1.register()

p2 = Person("wonhying", 23, "Feale", "nate.com")
p2.register()

print(p1.myinfo)
print(p2.myinfo)