import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Digite um número de 1 a 100: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentaivas!")
        break
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")