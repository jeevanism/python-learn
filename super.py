class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} speaks"


class Sparrow(Bird):
    def speak(self):
        return super().speak() + " as chirp chirp"


robin = Sparrow('robin')
print(robin.speak())


class Ostrich(Bird):
    def speak(self):
        return f"{self.name} speaks Boom Boom"


class Crow(Bird):
    def speak(self):
        return super().speak() + f" as Caw Caw"


emmanuel = Ostrich('Emmanuel')
print(emmanuel.speak())

john = Crow('John')
print(john.speak())


class FlyingBird(Bird):
    def fly(self):
        return f" and {self.name} can fly"


class SwimmingBird(Bird):
    def ability(self):
        return f"  {self.name} can swim"


class Swan(SwimmingBird, FlyingBird):
    def feature(self):
        return super().speak() + " woo woo " + super().ability() + super().fly()


lenny = Swan('lenny')
print(lenny.feature())
