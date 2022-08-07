while True:
    try:
        c=0
        SUM=0
        for i in range(int(input())):
            a=input().split()
            c+=int(a[1])
            SUM+=(int(a[0])*int(a[1]))
        print('{:.4f}'.format(SUM/(c*100)))
    except:
        break
