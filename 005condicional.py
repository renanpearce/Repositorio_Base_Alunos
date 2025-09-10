# crie um codigo em phython que verifque se a senha digitada 
# pelo usuario for "1234", exiba "acesso permitido".

# etapas para resolução 
#criar uma variavel e a atriibuir a ela uma senha 
# atraves de um input solicitar a senha ao usuario
# atrasves de condicional checar se a senha é igual a senha armazenada 
# liberar ou não o acesso ao usuario 

senha1 = "1234"
senha = input("digite sua senha: ")

if senha == senha1:
    print("acesso liberado ")
else:
    print("a senha incorreta")
