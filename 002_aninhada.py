# 2. pariedade e tamanho do número
# crie um codigo python que receba um numero inteiro e informe:
# - se é par ou ímpar
# - e, ao mesmo tempo, se é maior que 10 ou menor ou igual a 10 
# utilize condicionais aninhadas para organizar as verificações

numero = int(input("digite seu numero"))
if numero % 2 == 0:
 if numero >= 10:
 
  print(f"o numero{numero} é par maior que 10")
 else:
  print(f"o numero{numero}é par menor que 10")
else:
  if numero >=10:
   print (f'o numero {numero} é impar e menor que 10 ')





