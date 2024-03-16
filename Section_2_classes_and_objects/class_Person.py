class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return print("I am", self.name)

    def greet(self):
        if self.age < 80:
            print("Hello World!, how are you doing?")
        else:
            print("Hello, how do you do")   
        self.display()         

person_1 = Person()
person_2 = Person()

person_1.set_details('Bob', 20)
person_2.set_details('Ted', 90)

#person_1.display()
person_1.greet()

#person_2.display()
person_2.greet()


