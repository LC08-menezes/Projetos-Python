nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print
print(f"Media: {media:.2f}")
print("Aluno:", nome)
if media >= 8:
  print("Aprovado")
elif media >= 4:
  print("Recuperação")
else:
  print("Reprovado")