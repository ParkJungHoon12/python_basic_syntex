class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def register(self):
        self.myinfo = self.name + " " + str(self.age) + " " + self.gender + " " + self.email + " " 



def sum(a,b):
    return a + b