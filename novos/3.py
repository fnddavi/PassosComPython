note1 = int(input("Nota 1: "))
note2 = int(input("Nota 2: "))
note3 = int(input("Nota 3: "))

media = (note1 + note2 + note3) / 3

if media >= 7:
    print(f"Aluno aprovado com média {media:.2f}")
elif media >= 6:
    print(f"Aluno em recuperação com média {media:.2f}")
else:
    print(f"Aluno reprovado com média {media:.2f}")
