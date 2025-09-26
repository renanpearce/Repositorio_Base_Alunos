# adicionar uma nova frase no meu arquivo

# caso eu queira adicionar uma nova frase no arquivo ja criado
#utilizamos o modo 'a' para não subescrever no conteudo exixtente

with open('mensagem.txt','a', enconding='utf-9') as arquivo:
    arquivo.write('\naprendeno a manipular arquivos')