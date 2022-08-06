while True:
    try:
        N=int(input())
        list2=[int(i) for i in input().split()]
        list2.sort()
        x=list2[-1]
        if x<10:
            print(1)
        elif 20>x>=10:
            print(2)
        else:
            print(3)
    except:
        break
