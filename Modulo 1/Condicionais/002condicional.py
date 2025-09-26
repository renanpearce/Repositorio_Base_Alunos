# crie um código que receba 3 notas, calcule a media 
# e informe se o aluno esta aprovado, em recuperação
# ou reprovado 
# etapas
# OBS: aprovado >= 7
#recuperação media > 4 
#reprovado < 4


#  1) solicitar as notas ao usuario 
# 2) calcular media
# 3) checar a condiçao do aluno 
# 4) infomar os resultados 

#etapas
# 1) solicitar  as notas ao usuario 
n1=float(input("digite a primeira nota:"  ))
n2 = float(input ("digite a n2: "))
n3  = float(input("digite a n3:"))

# 2)calcular media
media = (n1 + n2 + n3)/3

# 3) checar a condição do aluno 
if media >=7:
    print(f"o aluno tem media {media:.2f} e esta aprovado. ")
elif media > 4:
    print(f"o aluno teve media {media: . 2f} e esta de recuperação.")

else:
    print(f"o aluno teve media {media:.2f} e esta reprovado")
