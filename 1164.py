N=int(input())
for i in range(N):
    a=int(input())
    SUM=0
    for j in range(1,a):
        if a%j==0:
            SUM+=j
    if SUM==a:
        print(a,'eh perfeito')
    else:
        print(a,'nao eh perfeito')
