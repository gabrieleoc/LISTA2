print("Lista do Supermercado.")

lista1 = []

n = 1

while True:
    pergunta = input("O que deseja adicionar a lista?\n")
    lista1.append(pergunta)
       
    if n == 5:
        break
    
    n += 1
    
imprimir = input("Deseja ver os itens na lista? S/N\n")

if imprimir == 'S':
    print(f"Sua lista de compras:\n{lista1}")
elif imprimir == 'N':
    print('Até mais!')
else:
    print("Resposta errada reinicie o programa.")
