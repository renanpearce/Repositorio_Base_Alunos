# crie um código python que verefique se 
# o ano é bissexto ou não

ano = int(input("digitar um ano:"))

if ano % 4 == 0:
    if ano % 100 != 0 or ano % 400 == 0:
        print(f"o ano {ano} é bissexto.")
    else:
        print(f"o ano {ano} não é bissesxto")
else:        
    print(f"o ano {ano} não é bissexto")
