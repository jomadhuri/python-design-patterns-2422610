Class Dog:
  def __init__(self, name):
    self.name = name
    
  def speak(self):
    return "Woof!"
  
Class Cat:
  def __init__(self, name):
    self.name = name
    
  def speak(self):
    return "Meow!"
  
def get_pet(pet):
  pets = dict()
  pets = {dog: Dog("Marley"), cat: Cat("Kitty")}
  return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
