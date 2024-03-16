class Car:
    def __init__(self, color, model_type):
        self.color = color 
        self.model_type = model_type
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 5

# create an instance of the class Car
car1 = Car('red', 'Sedan')                
car2 = Car('blue', 'SUV')

# Accessing attributes and calling instance methods
print(f'Color of the first car: {car1.color}')
print(f'Model type of the second car: {car2.model_type}')


car1.accelerate()
print(car1.speed)

car2.brake()
print(car2.speed)