T=int(input())
for i in range(T):
    a=input()
    list1=a.split()
    PA=int(list1[0])
    PB=int(list1[1])
    GA=float(list1[2])
    GB=float(list1[3])
    count=0
    f=True
    while PA<=PB:
        PA+=int((PA*(GA/100)))
        PB+=int((PB*(GB/100)))
        count+=1
        if count>100:
            f=False
            break
    if f:
        print(count,'anos.')
    else:
        print('Mais de 1 seculo.')
