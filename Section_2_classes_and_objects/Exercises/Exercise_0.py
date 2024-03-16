'''
Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.
In the set_details method, create two instance variables : name and balance. The default value for balance should be zero. In the display method, display the values of these two instance variables.
Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from balance and inside deposit, add the amount to the balance.
Create two instances of this class and call the methods on those instances.
'''

class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name 
        self.balance = balance

    def display(self):
        print(self.name, self.balance)
 
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount


purchase1 = BankAccount()
purchase1.set_details("Amelia", 200)

purchase2 = BankAccount()
purchase2.set_details("Tom", 200)

purchase1.display()
purchase2.display()
        
purchase1.withdraw(50) 
purchase2.deposit(500)       

purchase1.display()
purchase2.display()