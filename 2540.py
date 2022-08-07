while True:
    try:
        N=int(input().strip())
        a=input().split()
        count=0
        for i in a:
            if i=='1':
                count+=1
        if (count/N)>=(2/3):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except:
        break
