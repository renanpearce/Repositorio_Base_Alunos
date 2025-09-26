# criar arquivo, recebendo informação do usuario

#  solicitação de entrada
nome = input('digite seu nome completo:')
email = input('digite seu e-mail')

# criar arquivo
arquivo = open('pessoa.txt','a',encoding='utf-8') # estamos criando o arquivo
# armazenando na variavel arquivo, o modo 'a' escreve sempre no final,
# enconding utf-8 é para utilizar o conjunto de caracteres que engloba
# a língua portuguesa
arquivo.write(nome+'|'+ email + '\n') # .write é para escrever e o 
# \n é para pular linha
arquivo.close() # .close é para fechar o arquivo