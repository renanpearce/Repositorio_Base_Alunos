import pyautogui
import webbrowser
import time 

# passo1 : abrir o youtube co uma musica específica
url = 'https://www.youtube.com/watch?v=VcRc2DHHhoM&list=RDVcRc2DHHhoM&start_radio=1'
webbrowser.open(url)

# passo 2: aguardar o carregamento da página
time.sleep(5) # ajustar de acordo com a velocidade da internt utilizada

# passo 3: garantir que o video come (aperte o espaço para 'play')
pyautogui.press('space') # toca ou pausa o video