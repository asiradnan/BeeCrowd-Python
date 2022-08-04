while True:
    M,N=[int(i) for i in input().split()]
    SUM=0
    if M>N and M>0 and N>0:
        for i in range(N,M+1):
            SUM+=i
            print(i,end=' ')
        print(f'Sum={SUM}')
    elif N>M and M>0 and N>0:
        for i in range(M,N+1):
            SUM+=i
            print(i,end=' ')
        print(f'Sum={SUM}')
    elif M<=0 or N<=0:
        break
