# leer o arquivo e exibir o texto em letras maiusculas

with open('mensagem.txt''r', enconding='utf-8') as arquivo:
    for linha in arquivo: # aqui percorremos as linhas do arquivo
        print(linha.strip().upper()) # imprimos cada linha em letras maisculas e
# tiramos os espaços