# solicitamos dois numeros ao usuario sem informar o tipo de dado
num1= input('digite o primeiro numero:')
num2 = input ('digite o sguno numero:')

try: 
    num1 = int(num1)
    num2 + int(num2)

    print(f'soma dos numeros {num1 + num2}')
except:
    print("digite um numero correto")


