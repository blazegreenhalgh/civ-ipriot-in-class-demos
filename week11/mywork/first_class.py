

class Cat:
    def __init__(self, name, age, coat_colour):
        self.name = name
        self.age = age
        self.coat_colour = coat_colour

    def meow(self):
        print(f"{self.name} meowed at you")

    def purr(self):
        print(f"{self.name} purrs")

    def meet(self, other):
        print(f"{self.name} hisses at {other.name}")



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks")

    def meet(self, other):
        if isinstance(other, Dog):
            print(f"{self.name} wags his tail!")
        else:
            print(f"{self.name} barks at {other.name}")


henrik = Cat('Henrik', 10, "Brown")
lev = Cat('Lev', 10, "Brown")
print(henrik.name, henrik.age, henrik.coat_colour)
henrik.meow()
henrik.purr()


vinnie = Dog('Vinnie', 2)
dog2 = Dog('dog2', 2)

print(vinnie.name, vinnie.age)

vinnie.bark()

# print(type(vinnie), type(henrik))

# print(isinstance(Dog, Cat))

henrik.meet(vinnie)
henrik.meet(lev)
vinnie.meet(henrik)
vinnie.meet(dog2)
