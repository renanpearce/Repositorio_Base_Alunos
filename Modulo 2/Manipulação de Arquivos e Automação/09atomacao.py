# desenhar um objeto
# apos a execução do código abra um bloco de notas
# para o desenho ser criado

import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('desenhando com pyautogui')
pyautogui.press('enter')
time.sleep(2)

arvore = [
'   ^    ',
    '  ^^^   ',
    ' ^^^^^  ',
    '  |||   ',
    '  |||   '

]

for linha in arvore:
    pyautogui.write(linha,interval=0.1)
    pyautogui.press('enter')
print('desenho da cara concluído')