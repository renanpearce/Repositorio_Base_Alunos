# croar um arquivo chamado mensagem.txt e escrever uma frase
# utilizando a with open() não precisamos utilizar o close() pois o arquivo será
# fechado ao final da execução
with open('mensagem.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('python facilite a vida!')