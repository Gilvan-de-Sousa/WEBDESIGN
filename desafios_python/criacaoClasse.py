class Dinossauro():
    def __init__(self, tipo, locomover):
        self.tipo = tipo
        self.locomover = locomover
        
    def mostrar(self):
        print(f"Nome do Dinossauro: {self.tipo}\nForma de locomoção: {self.locomover}")
        
dino1 = Dinossauro("Pterossauro", "Voo")
dino2 = Dinossauro("Tiranossauro", "2 patas")

dino1.mostrar()
print("")

dino2.mostrar()