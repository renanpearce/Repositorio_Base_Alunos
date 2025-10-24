import requests # essa biblioteca faz as requisições
import json # essa biblioteca le os arquivos json
import pyautogui # automação mouse e teclado
import time # controle de tempo
from bs4 import BeautifulSoup # interpretar o html

# 1. Url da página
url="https://www.cnnbrasil,.com.br"

# 2. faz a requisição HTTP
response = requests.get(url)
response.encoding = 'utf-8'

# 3. Use o Beautifulsoup para parsear o HTML
soup = BeautifulSoup(response.text,"html.parsear")

# 4. Extrair titulo e primeiro paragrafo
titulo = soup.tittle.string
primeiro_paragrafo = soup.find('p').text

# 5. exibir o titulo e o primeiro parágrafo
# print(f'titulo: {titulo})
# print(f'primeiro paragrafo: {primeiro_paragrafo}')

# 5. montar um dicionario python
dados={
    "titulo":titulo,
    "primeiro_paragrafo":primeiro_paragrafo
}

# 6. converte para json
dados_json = json.dumps(dados, indent=4 ,ensure_ascii=False)

# 7. salvar em arquivo json
with open('cnn_python.json','w', encoding='utf-8') as f:
    f.write(dados_json)

# 8. pyautogui imprime no terminal
print('abra o terminal e posicione o cursor, a digitação começa em 5 segundos...')
time.sleep(5)
pyautogui.write(dados_json, interval=0.01)