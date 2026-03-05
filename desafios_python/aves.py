class Ave():
    def __init__(self, tipo, cor, tamanho):
        self.tipo = tipo
        self.cor = cor
        self.tamanho = tamanho
        
    def __str__(self):
        return f"Tipo de Ave: {self.tipo}\nCor: {self.cor}\nTamanho: {self.tamanho}"
    
passaro1 = Ave("Papagaio", "Cinza", "Médio")

print(passaro1)
