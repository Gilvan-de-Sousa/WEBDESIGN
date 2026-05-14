# Melhorando CLASSES:
# Conta Bancária

class Gafanhoto:
    def __init__(self, nome = "Vazio", idade = 0): # Método Construtor
    # atributos de instância
        
        self.nome = nome
        self.idade = idade
        
    # Métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1
    
    
    def __str__(self): # Dunder method
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
    
# Declaração dos Objetos:

g1 = Gafanhoto("Maria", 17)

g1.aniversario()


print(g1)

g2 = Gafanhoto("Mauro", 15)


print(g2)

g3 = Gafanhoto()


print(g3)
print("")
print(g1.__dict__)
print(g1.__getstate__()) # Se apresenta da mesma forma que __dict__
print("")
print(g2.__getstate__())