class Veiculo():
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        
    def mostrarCarro(self):
        print(f"Veiculo Modelo: {self.modelo}\nCor: {self.cor}")
        
carro1 = Veiculo("Vectra", "Vermelho")
carro2 = Veiculo("Twingo", "Prata")

carro1.mostrarCarro()
print("")
carro2.mostrarCarro()

class Passaro():
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
    
    def cantar(self):
        print(f"Passaro: {self.tipo}\nCor: {self.cor}")
        
ave1 = Passaro("João de Barro", "Avermelhado")
ave2 = Passaro("Sabiá", "Preto, Alaranjado e Amarelo")

print("")
ave1.cantar()
ave2.cantar()