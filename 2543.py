while True:
    try:
        a=input().split()
        count=0
        for i in range(int(a[0])):
            b=input().split()
            if b[0]==a[1] and b[1]=='0':
                count+=1
        print(count) 
    except:
        break
