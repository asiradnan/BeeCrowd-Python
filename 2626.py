while True:
    try:
        win=['Os atributos dos monstros vao ser inteligencia, sabedoria...',"Iron Maiden's gonna get you, no matter how far!",'Urano perdeu algo muito precioso...']
        a=input().split()
        if a.count('papel')==2:
            if 'pedra' in a:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
            else:
                x=a.index('tesoura')
                print(win[x])
        elif a.count('pedra')==2:
            if 'tesoura' in a:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
            else:
                x=a.index('papel')
                print(win[x])
        elif a.count('tesoura')==2:
            if 'papel' in a:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
            else:
                x=a.index('pedra')
                print(win[x])
        else:
            print('Putz vei, o Leo ta demorando muito pra jogar...')
    except:
        break
