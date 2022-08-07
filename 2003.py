while True:
    try:
        x,y=[int (i) for i in input().split(':')]
        if x<7:
            print('Atraso maximo:',0)
        elif x==8:
            if y==0:
                print('Atraso maximo:',60)
            else:
                print('Atraso maximo:',y+60)
        elif x==9:
            print('Atraso maximo:',120)
        else:
            if y==0:
                print('Atraso maximo:',0)
            else:
                print('Atraso maximo:',y)
    except:
        break
