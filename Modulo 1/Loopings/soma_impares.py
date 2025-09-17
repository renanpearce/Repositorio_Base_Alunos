# crie um programa que some todos os numeros imparaes
#  que são multiplos de 3 a 1 a 30 e apresente o resultado
# etapas para resolução
# 1) criar um for de para captar os numeros impares 
# 2) criar uma condicional para checar se o numero é multiplo de 3
# 3) apresentar o resultados

soma = 0 

for i in range (1,31,2): # contagem dos numeros impares :
        if i % 3 == 0:
         print(i, end=',')
         multiplo_tres += i
print()
print(f"a soma dos numeros impares multiplos de 3 neste intervalo é {multiplo_tres}")
