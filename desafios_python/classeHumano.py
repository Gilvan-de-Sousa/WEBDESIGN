class Humano():
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        
    def Genero(self):
        print(f"Nome: {self.nome}\nSexo: {self.sexo}")
        if self.sexo[0] in "Mm":
            print("Pessoa do gerero masculino.")
        elif self.sexo[0] in "Ff":
            print("Pessoa do genero feminino.")
        
        

pessoa1 = Humano("Tulio", "Masculino")
pessoa2 = Humano("Gabriela", "Feminino")

pessoa1.Genero()
print("")
pessoa2.Genero()