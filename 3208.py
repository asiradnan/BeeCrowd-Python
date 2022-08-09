while True:
    a=input()
    if a=='0 0':
        break
    else:
        a=a.split()
        x=int(a[0])
        y=int(a[1])
        f=True
        def a():
            for i in range(2,y):
                if x%i==0:
                    return i
        p=a()
        if type(p)!=int:
            print('GOOD')
        else:
            print(f'BAD {p}')
