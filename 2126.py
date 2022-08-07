c=1
while True:
    try:
        a=input()
        b=input()
        print(f'Caso #{c}:')
        if a in b:
            d=b.count(a)
            print('Qtd.Subsequencias:',d)
            b=b.rfind(a)
            print('Pos:',b+1)
        else:
            print('Nao existe subsequencia')
        c+=1
        print()
    except:
        break
