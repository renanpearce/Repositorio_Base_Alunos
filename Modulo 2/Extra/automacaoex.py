import pyautogui
import time

# Espera 2 segundos antes de começar (para você ter tempo de ver o que acontece)
time.sleep(2)

# Pressiona as teclas Win + R para abrir o Executar
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Digita "calc" e pressiona Enter
pyautogui.typewrite('calc')
pyautogui.press('enter')
time.sleep(2)  # Espera a calculadora abrir

# Faz o cálculo 8 + 2
pyautogui.typewrite('8')
pyautogui.press('+')
pyautogui.typewrite('2')
pyautogui.press('enter')

# Espera um pouco e tira um print da tela (opcional)
time.sleep(2)
pyautogui.screenshot('resultado_calculadora.png')

print("Cálculo realizado! O resultado deve aparecer na tela da calculadora.")