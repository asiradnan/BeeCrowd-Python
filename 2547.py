while True:
    try:
        a=input().split()
        count=0
        for i in range(int(a[0])):
            b=int(input())
            if int(a[1])<=b and b<=int(a[2]):
                count+=1
        print(count)
    except:
        break
