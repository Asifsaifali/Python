class Animal():
  
  def __init__(self,color,size,name):
    self.color = color
    self.size = size
    self.name = name
  
  def GetDetails(self):
    return f"{self.name} has {self.color} color"

animal = Animal("Black",56,"Dog")
print(animal.GetDetails())
