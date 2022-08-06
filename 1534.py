while True:
    try:
        a=int(input())
        if a%2==0:
            x=a
            for i in range(int(a/2)):
                empty='1'+(x-2)*'3'+'2'
                print(empty.center(a,'3'))
                x-=2
            for i in range(int(a/2)):
                empty='2'+(x)*'3'+'1'
                print(empty.center(a,'3'))
                x+=2
        else:
            x=a
            for i in range(int(a/2)):
                empty='1'+(x-2)*'3'+'2'
                print(empty.center(a,'3'))
                x-=2
            empty='2'
            print(empty.center(a,'3'))
            for i in range(int(a/2)):
                empty='2'+(x)*'3'+'1'
                print(empty.center(a,'3'))
                x+=2
    except:
        break
