for i in range(int(input())):
    a=input().split()
    k=int(a[1])
    b=int(a[0])
    c=b//k
    c+=b%k
    print(c)
