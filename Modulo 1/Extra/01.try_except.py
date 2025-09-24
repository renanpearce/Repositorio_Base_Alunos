# utilizamos o try/except para apresentar uma exceção
# de uma maneira mais amigavel ao usuario
 
try:# o codigo tenta executar o comando
    resultado = 10/0
except: # caso não consiga, ele apresenta qual é o erro
    print('ocorreu um erro na operação. não é possivel a divisão com denoinador igual a zero')