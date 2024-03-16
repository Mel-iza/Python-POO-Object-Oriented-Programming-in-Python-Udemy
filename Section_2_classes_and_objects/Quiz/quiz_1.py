class Test:
    def method1(self):
        print('Inside Method1')

    def method2(self):
        print('Inside Method1')
        self.method1()
    

t = Test()
t.method2()

print(t.method2())
