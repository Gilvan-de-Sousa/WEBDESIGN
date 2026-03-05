class Veiculos():
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
    
    def __str__(self):
        return f"Marca: {self.marca}\nCor: {self.cor}\nModelo: {self.modelo}"
    
veiculo1 = Veiculos("Volkswagen", "Prata", "Golf")

print(veiculo1)
print(" ")

veiculo2 = Veiculos("Citroen", "Vermelho", "C3")
print(veiculo2)
        