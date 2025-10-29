
import requests

# definir o nome para consulta
nome = input('digite o nome da pessoa').strip()

# url da api
url = f'https://api.agify.io/?name={nome}'

# fazer a requisição
response = requests.get(url)

# processar a resposta
if response.status_code == 200:
    dados = response.json()
    print(f'nome:{dados['name']}')
    print(f'idade estimada:{dados['age']} anos')
    print(f'numero de registros analisando: {dados['count']}')
else:
    print(f'erro ao acessar a API:{response.status_code}')