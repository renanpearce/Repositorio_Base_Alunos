# solicite ao usuario 4 notas
# calcule a média 
# informe se o aluno está aprovado (media>=7), recuperação (5<media<7) ou reprovado
# apresente as notas que o aluno tirou, a media e o status de sua situação

#lista
# for 
# if/elif/else
notas = []

for i in range(4):
    nota = float(input(f'informe a nota da prova {i+1}'))
    if nota > 0:
        notas.append(nota)
    else:
        print("valor inválido")
print(f"suas notas são: {notas}") # linha opcional
media = sum(notas)/len(notas)

if media >=7:
    print(f"suas notas foram {notas}, sua {media:.2f} e voce esta aprovado")
elif 5 <= media < 7:
    print(f"suas notas foram {notas}, sua {media:.2f} e voce esta de recuperação") 
else: # notas abaixo de 5, ou seja, de 4,99 para baixo
    print(f"suas notas foram{notas}, sua {media:.2f} e voce esta aprovado")

