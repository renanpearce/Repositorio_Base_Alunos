# Criar um código que consuma uma api de clima informe
# a temperatura e a descrição do clima em lugar específico

# etapa
# 1. definir chave de API e o link da requisição
import requests

api_key = '2a1ac38a32354cb7b19133643251408'
cidade = input('digite o nome da cidade:').strip() # input para receber a informação do usúario e a função
# strip() tira os espaços
url= f'https://api.weatherapi.com/v1/current.json'

# 2. parametros da requisição
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt' # define a língua da resposta como portugues
}

# 3. fazer a requisição
resposta = requests.get(url,params=parametros) # utilizamos o método get e informamos os parametrso dessa requisição

# 4. verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json() # convertendo a resposta JSON em um dicionário python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'temperatura na cidade {cidade} é {temperatura}°C.')
    print(f'descrição: {descricao}')
else:
    print(f'erro na requisição: {resposta.status_code}')
    print(resposta.content)