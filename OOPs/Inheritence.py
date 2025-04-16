class Parent:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    
    def GetDetails(self):
        return f"The name is {self.name} and age is {self.age} & address is {self.address}"
    
class Son(Parent):

    def __init__(self,name, age, address, hoobies, Cars):
        super().__init__(name, age, address)
        self.hoobies = hoobies
        self.Cars = Cars
son = Son("Asif", 22, "Delhi", "Don't know", "RR")
print(son.GetDetails() +" with hoobies of " + son.Cars)
