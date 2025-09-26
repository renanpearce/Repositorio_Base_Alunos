# crie um codigo em phythonque peça o valor da conta. se for maior que R$ 100,00
# adicione uma gorjeta de 10% e exiba o valor total a pagar 
# # caso contrario, adicione uma gorjeta 5%

# etapas para solução
# 1) solicitar o valor da conta para o usuario 
# 2) se a conta for maior que 100 adicione 10% de gorjeta e apresentar o total a pagar 
# 3) se a conta for menor que 100 adicionar 5% de gorjeta e apresenrtar o total a pagar

conta = float(input("o valor de sua conta"))
if conta >=100:
    fechamento=conta +(conta *0.1)
    print('fechamento{fechamento:.2f}')
else:
    fechamento = conta +(conta*0.05)
    print(fechamento)
