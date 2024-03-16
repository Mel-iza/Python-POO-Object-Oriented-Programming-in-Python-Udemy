class Test:
    def method1(self):
        self.x = 10

    def display(self):
        self.method1() # Chama o método method1 para definir o valor de x
        print(self.x)  # Imprime o valor de x

t = Test()
t.display()

'''
o valor de x não está sendo impresso porque o método display está tentando imprimir o resultado da chamada de self.method1(), que não retorna nada explicitamente. O método method1 simplesmente define o atributo x da instância atual como 10, mas não retorna nenhum valor.
'''