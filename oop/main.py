class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def bark(self):
        print(f"{self.name} is barking")

    
class Beagle(Dog):
    def __init__(self, name, age, gender, is_hunter):
        super().__init__(name, age, gender)
        self.is_hunter = is_hunter

    def hunt(self):
        print(f"{self.name} is hunting so good")


b1 = Beagle("jessi", 12, "girl", True)
b1.bark()
b1.hunt()