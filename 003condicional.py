# criar um codigo phython que indique a temperatura esta agradavel ou nao 
#condições:
# temperatura >= 30° informar que esta muito quente 
# temperatura >=20° informar que a temperatura agradavel 
# temperatura >= 10° informar que esta muito frio
# temperatura abaixo de 10°informar que esta muito frio 

# etapas para resolução:
# 1) solicitar temperatura ao usuario
# 2)verificar condicional
# 3) imprimir a reposta segunda a temperatura   

temperatura = float (input("digite a temperatura do dia:"))

# if condição:

if temperatura >=30:
    print(f"a temperatura do dia é {temperatura}°C e o dia esta muito quente ")
elif temperatura >= 20: 
    print(f"a temperatura do dia é {temperatura}°C e o dia esta agradavel. ")
elif temperatura >= 10:
    print(f"a temperatura do dia é {temperatura}°C e o dia esta muito frio ")
else: 
    print(f"a temperatura do dia é {temperatura}°C e o dia esta um lixo ")
