#3042
while True:
    main=[]
    e=int(input())
    if e==0:
        break
    else:
        for i in range(e):
            a=[int(j) for j in input().split()]
            main.append(a)
        index=1
        count=0
        for row in range(len(main)):
            if main[row].index(0)==index:
                pass
            else:
                if main[row].count(0)==1:
                    count+=abs(main[row].index(0)-index)
                    index=main[row].index(0)
                elif main[row].count(0)==2:
                    minimum=4
                    temp=None
                    for x in range(3):
                        if x!=index:
                            if abs(main[row].index(0)-index)<minimum and abs(main[row].index(0)-index)!=0:
                                minimum=abs(main[row].index(0)-index)
                                temp=x
                    count+=minimum
                    index=temp
        print(count)
