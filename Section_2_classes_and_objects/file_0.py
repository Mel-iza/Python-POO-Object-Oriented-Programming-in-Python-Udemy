class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return print("String here")

    def greet(self):
        print("Hello World!")    

person_1 = Person()
person_2 = Person()

person_1.display()
person_1.greet()

person_1.set_details()
person_2.set_details()

