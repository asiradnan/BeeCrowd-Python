while True:
    try:
        from datetime import date
        c=date(2016,12,25)
        a=input().split()
        b=date(2016,int(a[0]),int(a[1]))
        x=(c-b).days
        if x<0:
            print('Ja passou!')
        elif x==0:
            print('E natal!')
        elif x==1:
            print('E vespera de natal!')
        else:
            print(f'Faltam {x} dias para o natal!')
    except:
        break
