SUM=0
went=0
while True:
    a=input().split()
    if a[0]=='ABEND':
        print(SUM)
        print(went)
        break
    elif a[0]=='SALIDA':
        SUM+=int(a[1])
        went+=1
    else:
        went-=1
        SUM-=int(a[1])
