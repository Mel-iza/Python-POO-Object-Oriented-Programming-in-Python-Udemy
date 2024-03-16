class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"I am {self.name} and i'm {self.age} years old")

    def greet(self):
        if self.age < 80:
            print("Hello World!, how are you doing?")
        else:
            print("Hello, how do you do")   
        self.display()         

person_1 = Person('Amelia', 54)
person_2 = Person('Jonas', 78)

person_1.display()
person_1.greet()

person_2.display()
person_2.greet()


