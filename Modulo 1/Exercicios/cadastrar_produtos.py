# cadastro de produtos com relatorio
# crie um pograma em phython que permita cadastrar produtos
# salver essas infromações em um arquivo chamado produtos.txt
# o programa deve permitir:
# 1) inserir o nome do produto e preço
# 2) gravar os produtos no arquivo (um por linha)
# 3)ler os dados do arquivo e gerar um relatório com:
# - lista de produtos cadastrados
# - média dos preços
# - o produto mais caro e mais barato

# criar o arquivo produtos.txt e escrever os produtos
with open('produtos.txt ', 'w', encoding='utf-8') as arquivo:
    arquivo.write('cafe, 36.00\n')
    arquivo.write('chá, 10.00\n')
    arquivo.write('suco,18.50\n')
    arquivo.write('refrigerante, 17.50\n')
    arquivo.write('água, 5.50\n')

# ler os produtos do arquivo
produtos =[]
with open('produtos.txt','r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome,preco = linha.strip().split(',')
        produtos.append((nome,float(preco)))

# calcular a media , o mais caro e o mais barato
total = 0
mais_caro = produtos[0]
mais_barato = produtos[0]

for nome, preco in produtos:
    total+=preco # percorre a lista produtos e soma cada preço encontrado
    if preco > mais_caro[1]:
        mais_caro = (nome, preco)

        if preco < mais_barato[1]:
            mais_barato = (nome, preco)

media= total/len(produtos)

# criar o relátoria 
with open('relatorio_produtos.txt', 'w', encoding='utf-8') as relatorio:
    for nome, preco in produtos:
        relatorio.write(f'{nome}: R${preco:.2f}')

        relatorio.write(f'\npreco medio: R$ {media:.2f}\n')
        relatorio.write(f'produto ,ais caro: {mais_caro[0]} R${mais_caro[1]:.2f}\n')
        relatorio.write(f'produto mais barato: {mais_barato[0]}R${mais_barato[1]:.2f}\n')
