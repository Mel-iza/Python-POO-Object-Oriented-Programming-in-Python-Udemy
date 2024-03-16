## Classes and objects
---
- Execution of a class statement creates a class object and binds it to the class name
- Instantiation of the class creates new instance objects
- Instance objects are first class objects in Python
- Class objects are also first class objects in Python
- Methods are defined inside the class using def statement
- Inside the method definition, the first parameter shoud be `self`
- Instance variables can be created inside any method, by assigning to a variable name prefized with `self`. Example: `self.variablename = value`
- To reference an instance variable inside any method, you have to prefix the variable name with `self`. Example: `print(self.variablename)`
- To call a method inside another method, you have to prefiz the method name with `self.`Example: `self.methodname()`
- The class object is created when the class definition is executed
- In a method definition, the parameter self refers to the <b>instance object that invokes the method</b>
- Instantiation of the class creates a new instance object

#### Self notes
- Uma classe é um 'modelo' que define as características e comportamentos de objetos.
- Uma instância é um objeto específico criado a partir de uma classe. A classe seria a concepção do objeto, enquanto a instância é a concretização 'física' do objeto, ou manifestção/criação.
- Cada instância têm seu próprio conjunto de atributos (características) e métodos (ações).
