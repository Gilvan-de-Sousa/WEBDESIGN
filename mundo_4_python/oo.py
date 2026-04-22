class Gafanhoto:
    def __init__(self):
        # atributos de instância
        
        self.nome = ""
        self.idade = 0
        
        # Métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1
        
    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    

g1 = Gafanhoto()

g1.nome = "Maria"
g1.idade = 12
g1.aniversario()


print(g1.mensagem())

g2 = Gafanhoto()

g2.nome = "Mauro"
g2.idade = 15

print(g2.mensagem())

