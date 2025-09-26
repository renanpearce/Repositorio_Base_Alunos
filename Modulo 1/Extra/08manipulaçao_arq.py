# contar quantas linhas tem no arquivo

with open('pessoa.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines() # aqui estamos lendo o arquivo e armazenando
# a leitura na variável linhas
    print(f'total linhas:', len(linhas)) # na função len() conta quantas
    # linahs tem no arquivo lido