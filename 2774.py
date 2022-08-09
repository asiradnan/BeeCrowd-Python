while True:
    try:
        SUM=0
        a=[int(i) for i in input().split()]
        QT=int((a[0]*60)/a[1])
        a=[float(i) for i in input().split()]
        mean=sum(a)/len(a)
        for x in a:
            SUM+=((x-mean)**2)
        abc=(SUM/(QT-1))**.5
        print('{0:.5f}'.format(abc))
    except:
        break
