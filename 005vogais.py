# peça ao usuario para digitar uma letra
# se for vogal, informe qual vogal
# se for consoante, verifique se é maiscula ou minuscula 

# solicitação de entrada de dados do tipo string (texto)
letra = input("digite uma letra:")

if letra.lower() in "aeiou": #.lower() transforma para minuscula
    print(f"vogal: {letra}")
else:
    if letra.isupper(): # isupper identifica se a letra esta em maiscula
        print(f"consoante maiuscula: {letra} ")
    else: 
        print(f"consoante minuscula:{letra}")