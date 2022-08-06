while True:
    try:
        a=int(input())
        b=int(a/3)
        x=a-2
        for i in range(b):
            empty='2'+x*'0'+'3'
            print(empty.center(a,'0'))
            x-=2
        x+=2
        d=int(x/2)
        for i in range(d):
            empty=('1'*x)
            print(empty.center(a,'0'))
        empty='4'
        empty=empty.center(x,'1')
        print(empty.center(a,'0'))
        d=int(x/2)
        for i in range(d):
            empty=('1'*x)
            print(empty.center(a,'0'))
        for i in range(b):
            empty='3'+x*'0'+'2'
            print(empty.center(a,'0'))
            x+=2
        print()
    except:
        break
