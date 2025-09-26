# crie um codigo em phython que peça um numero ao usuario
# e exiba "numero" par se ele for dvisivel por 2 

# etapas de resolução 

# 1) solicitar um numero ao usuario 
# 2) Verificar se o numero é par ou impar 
# 3) informar se o numero é par ou impar 

numero = float(input("digite seu numero"))

if numero % 2 == 0:
  print(f"o numero {numero} é par.")
else:
  print (f'o numero {numero} é impar. ')
