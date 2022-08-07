while True:
    T=int(input())
    if T==0:
        break
    else:
        for i in range(T):
            a=int(input())
            if a%2==0:
                print((a*2)-2)
            else:
                print((a*2)-1)
