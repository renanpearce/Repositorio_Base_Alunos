# crie uma automação que escreve um texto automaticamente 

import pyautogui
import time

# obeservevação: abra um bloco de notas vazio
# aguarde 5 segundos para voce abrir o blobo de notas
time.sleep(5)

# escreva o texto 
pyautogui.write('Automatizando com pyautogui', interval=0.1)