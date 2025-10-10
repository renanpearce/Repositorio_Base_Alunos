# efeito "matrix" no bloco de notas
# após executar o código abra um bloco de notas novo

import pyautogui, time, random

time.sleep(3)
chars = '01'
for i in range(20):
    pyautogui.write(random.choice(chars), interval=0.02)