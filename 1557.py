while True:
    main=[]
    x=int(input())
    if x==0:
        break
    else:
        temp2=[]
        for i in range(x):
            main.append(str(2**i))
        temp2.append(main)
        for j in range(1,len(main)):
            temp=[str(main[j])]
            for k in range(j,j+x-1):
                temp.append(str(2**(k+1)))
            temp2.append(temp)
        ab=len(temp2[-1][-1])
        for row in temp2:
            for col in range(len(row)):
                if col!=len(row)-1:
                    print(row[col].rjust(ab),end=' ')
                else:
                    print(row[col].rjust(ab))
        print()
