N=int(input())
for i in range(N):
    a=int(input())
    count=0
    for j in range(1,a):
        if a%j==0:
            count+=1
    if count==1:
        print(a,'eh primo')
    else:
        print(a,'nao eh primo')
