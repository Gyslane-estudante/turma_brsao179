#Tabuada

num = int(input("Digite um número para ver a tabuada: "))
print(f"\nTabela do número {num}")

for indice in range(1, 11):
    result = num * indice
    print(f"Número {num} x {indice} = {result}")
    print("\n" + "="*40)