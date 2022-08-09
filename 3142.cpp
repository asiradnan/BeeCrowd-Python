while True:
    try:
        SUM=0
        a=input()
        if len(a)==3:
            SUM+=(((ord(a[0])-64)*26*26)+((ord(a[1])-64)*26)+ord(a[2])-64)
            if SUM>16384:
                print('Essa coluna nao existe Tobias!')
            else:
                print(SUM)
        elif len(a)==2:
            print(((ord(a[0])-64)*26)+ord(a[1])-64)
        elif len(a)==1:
            print(ord(a)-64)
        else:
            print('Essa coluna nao existe Tobias!')
    except:
        break
