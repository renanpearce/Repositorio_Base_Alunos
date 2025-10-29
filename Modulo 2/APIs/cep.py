# crie uma api que consulte o cep e informe o endereço

# inicamos fazendo a importação da biblioteca requets
import requests
# indicamos a url para consulta da api
cep = input("digite o cep (somente numeros):") # usuarios informa o cep que deseja consultar
url = f'https://viacep.com.br/ws/{cep}/json/' # endereço de url formato para pesquisa do cep

# fazemos a requição
resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP {dados['cep']}')
        print(f'logradouro: {dados['logradouro']}')
        print(f'bairro: {dados['bairro']}')
        print(f'cidade: {dados['localidade']}')
        print(f'estado: {dados['uf']}')
    else:
        print('cep não foi encontrado')
else:
    print(f'erro na requsição: {resposta.status_code}')
    print(resposta.content)