num_secreto = 7
max_tentativas = 3

print(f"Tente adivinhar um número de 1 a 10!")
print(f"Você tem {max_tentativas} tentativas")

for i in range(1, max_tentativas + 1):
    palpite = int(input(f"Tentativa: {i}: "))

    if palpite == num_secreto:
        print("Parabéns! Você acertou o número em ", {i}, "tentativas")
        break
    elif palpite < num_secreto:
        print("O número é MAIOR!")
    else:
        print("O número é MENOR!")

    if i == max_tentativas:
        print(f"Suas tentativas acabaram, o número era {num_secreto}")