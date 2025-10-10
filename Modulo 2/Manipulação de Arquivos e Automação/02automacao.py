
# crie uma automação que faça o mouse se mover na forma de um quadrado
# importamos a biblioteca pyautogui
import pyautogui

for i in range (10):
    pyautogui.moveTo(100 + 10 *i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.25) 