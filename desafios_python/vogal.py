def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    cont = 0
    char = 0
    
    for  char in texto:
        if char in vogais:
            cont += 1
    return cont  


print(conta_vogais("Exemplo de texto com vogais"))