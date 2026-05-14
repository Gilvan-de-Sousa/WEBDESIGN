class ContaBancaria:
    """Criar uma conta bancária que permite fazer saques e depósitos"""
    
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        
    def __str__(self):
        return f"Número da conta: {self.id}, Nome do Titular: {self.titular}, Saldo: R$ {self.saldo:,.2f}"
    
    def depositar(self, valor):
        self.valor = valor
        self.saldo += valor
        print(f"Deposito de R$ {self.valor:,.2f} autorizado na conta {self.id}")
    
    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de R${valor:,.2f} negado na conta {self.id}! \nSaldo insuficiente!")
        
        self.valor = valor
        self.saldo -= valor
        print(f"Saque de R$ {self.valor:,.2f} autorizado na conta {self.id}")
   
# Criação e Uso de Objeto:
 
c1 = ContaBancaria(112, "Gustavo",  5400)
c1.depositar(500)

print(c1)

c1.sacar(10000)

print("")
print(c1)
print("")