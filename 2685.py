while True:
    try:
        a=int(input().strip())
        if a==360:
            print('Bom Dia!!')
        elif 0<=a<90:
            print('Bom Dia!!')
        elif 90<=a<180:
            print("Boa Tarde!!")
        elif 180<=a<270:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')
    except:
        break
