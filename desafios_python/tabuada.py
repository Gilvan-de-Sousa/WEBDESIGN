class Calculadora():
    def mult(self, a, b):
        self.a = a
        self.b = b
        return a * b
    
    def div(self, a,  b):
        self.a = a
        self.b = b
        return a / b

    def soma(self, a, b):
        self.a = a
        self.b = b
        return a + b
    
    def subt(self, a, b):
        self.a = a
        self.b = b
        return a - b

escolha = int(input(("Escolha uma operação:\n[1]Multiplicação\n[2]Divisão\n[3]Soma\n[4]Subtração\nOpção: ")))
print("-------------------xxxxxxxxxxxxxxxxxxxx-------------------")
print(" ")

a = int(input("Informe o 1º valor: "))
b = int(input("Informe o 2º valor: "))

calc = Calculadora()
if escolha == 1:
    print(calc.mult(a, b))
elif escolha == 2:
    print(calc.div(a, b))
    
elif escolha == 3:
    print(calc.soma(a, b))
elif escolha == 4:
    print(calc.subt(a, b))
    
else:
    print("Escolha inválida!")
