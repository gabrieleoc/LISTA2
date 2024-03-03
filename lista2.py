print("Lista do Supermercado.")

lista_de_compras = []

for _ in range(5):
    item = input("O que deseja adicionar a lista?\n")
    lista_de_compras.append(item)

imprimir = input("Deseja ver os itens na lista? (S/N)\n").upper()

if imprimir == 'S':
    print("Sua lista de compras:")
    for item in lista_de_compras:
        print(f"- {item}")
elif imprimir == 'N':
    print('Até mais!')
else:
    print("Resposta inválida. Por favor, reinicie o programa.")