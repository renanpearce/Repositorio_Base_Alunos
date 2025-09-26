# ler e imprimir o conteudo do arquivo mensaem.txt

with open('mensagem.txt','r, encoding=utf-8') as arquivo:
    print(arquivo.read()) # aqui estamos imprimindo o que arquivo leuna memória
# e neste caso, nao estamos armazenando em nenhuma variavel
