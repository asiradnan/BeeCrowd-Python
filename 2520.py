while True:
    try:
        a=input().split()
        mylist=[]
        f=False
        cap1=None
        cap2=None
        x=None
        y=None
        for i in range(int(a[0])):
            b=input().split()
            list1=[int(j) for j in b]
            if 1 in list1 and 2 in list1:
                mylist=list1.copy()
                f=True
            elif 1 in list1:
                mylist.append(list1)
                cap1=i
                x=list1.index(1)
            elif 2 in list1:
                mylist.append(list1)
                cap2=i
                y=list1.index(2)
        if f:
            print(abs(mylist.index(1)-mylist.index(2)))
        else:
            SUM=abs(cap1-cap2)
            SUM+=abs(y-x)
            print(SUM)
    except:
        break
