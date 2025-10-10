 # 1 passo: instalar o Pyautogui com o comando:
# pip install pyautogui

# crie uma automação que abra automaticamente um navegador

# importamos a biblioteca para o script em uso

# importamos a biblioteca para o script em uso
import pyautogui

# 'press' é um vomando que utilizamos 
# para pressionar a tecla desejada
pyautogui.press('win') # para pressionar a tecla windows

# 'slepp' é um comando que utilizamos para deixar o código
# em espera por alguns segundos
pyautogui.sleep(1)

# write é um comando que utilizamos para passar o que queremos 
# escrever
pyautogui.write('google chrome')

pyautogui.press('enter')