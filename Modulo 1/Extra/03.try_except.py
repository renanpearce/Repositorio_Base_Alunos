# crie uma função chamada calculadora que receba tres parametros:
#  dois numeros e uma operação(=,-,*,/)
# a função deve retornar o resultado da operação, mas precisa
# tratar as seguintes exceções:
#divisão por zero(zerodivisionError)
# tio de dado inválido (value error)

def calculadora():
    try:
        n = input('Digite um número ou x para sair do sistema: ')
        if n.lower() == 'x':
            print('Até breve.')
            return

        n1 = input('Digite outro número ou x para sair do sistema: ')
        if n1.lower() == 'x':
            print('Até breve.')
            return

        operador = input('Informe um operador matemático (+, -, *, /) ou x para sair do sistema: ')
        if operador.lower() == 'x':
            print('Até breve.')
            return

        # Converte para número
        n = float(n)
        n1 = float(n1)

        # Verifica operador
        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1
        elif operador == '*':
            resultado = n * n1
        elif operador == '/':
            if n1 == 0:
                raise ZeroDivisionError('Não é possível dividir por zero.')
            resultado = n / n1
        else:
            print('Você não escolheu um operador válido.')
            return

        print(f'Operação: {n} {operador} {n1} = {resultado}')

    except ValueError:
        print('Você digitou um caracter inválido, digite somente números.')
    except ZeroDivisionError as zero:
        print(zero)

calculadora()

