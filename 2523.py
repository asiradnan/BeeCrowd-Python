while True:
    try:
        a=input()
        input()
        empty=''
        b=input().split()
        c=[int(i) for i in b]
        for j in c:
            empty+=a[j-1]
        print(empty)
    except:
        break
