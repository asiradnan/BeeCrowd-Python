while True:
    a=int(input())
    count=1
    SUM=0
    if a!=0:
        while count<=5:
            if a%2==0:
                SUM+=a
                count+=1
            a+=1
        print(SUM)
    else:
        break
