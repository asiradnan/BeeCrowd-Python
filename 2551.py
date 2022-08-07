while True:
    try:
        MAX=0
        for i in range(int(input())):
            a=input().split()
            if (int(a[1])/int(a[0]))>MAX:
                MAX=(int(a[1])/int(a[0]))
                print(i+1)
    except:
        break
