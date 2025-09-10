# classificação por idade
# faça um programa que leia a idade de uma pessoa e classifique-a em:
# criança : menor 12 anos 
# adolescente: entre 12 a 17 anos
# adulto: maior ou igual a 18 anos
# utilize a estrtura de condicionl aninhada

idade = int(input("digite sua idade"))

if idade > 0: 
  if idade >= 18: 
    print(f"voce tem{idade} anos e é adulto.")
  elif 12 <= idade <=17:
    print(f"voce tem {idade} e é adolescente")
  else:
    print(f"voce tem {idade} e é uma criança")
else:
  print("idade não pode ser negativa, digite uma idade valida")     


  