while True:
    x=input()
    if x=='0':
        break
    else:
        a,b,c=tuple([int(i) for i in x.split()])
        d=a*b*(100/c)
        def x():
            for i in range(int(d)):
                if i*i>d:
                    return (i-1)
        print(x())
