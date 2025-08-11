# conceito: listas
# T17 GRUPO 1: Lavinia. Erik, Paulo, Vinicius, Lorena, Marcos, Lucas

# criando lista de compras
lista_de_compras = ["maçã", "banana", "laranja", "maçã", "tofu"] 
print(f"lista de compras inicial {lista_de_compras}")

# acesando o primeiro elemento da lista
print(f"primeiro elemento da lista: {lista_de_compras[0]}")

# acessando o último elemento 
print(f"últmo elemento da lista: {lista_de_compras[-1]}")

# adiciona um elemento no final da lista
lista_de_compras.append("miojo")
print(f"lista com o miojo adicionado: {lista_de_compras}")

# remove a primeira vez que encontra o elemento na lista
lista_de_compras.remove("maçã")
print(f"lista de compras sem a primeira maçã: {lista_de_compras}")

# remove e retorna o último elemento da lista 
removido = lista_de_compras.pop()
print(lista_de_compras)
print(f"item removido: {removido}")

# ordena a lista de compras em ordem alfabética
lista_de_compras.sort()
print(f"lista de compras ordenada alfabeticamente {lista_de_compras}")
