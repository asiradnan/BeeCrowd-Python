main=[]
SUM=0
for i in range(int(input())):
    a=[int(j) for j in input().split()]
    main.append(a)
SUM+=sum(main[-1])
main.pop(-1)
main2=[]
for col in range(len(main)+1):
    empty=[]
    for row in range(len(main)):
        empty.append(main[row][col])
    main2.append(empty)
print(main2)
x=len(main2)
for y in range(x-1):
    if y==x-2:
        
    minimum=100000
    for row in main2:
        if sum(row)<minimum:
            minimum=sum(row)
            index1=main2.index(row)
        elif sum(row)==minimum:
            if main2[index1][0]>row[0]:
                minimum=sum(row)
                index1=main2.index(row)
    SUM+=minimum
    main2.pop(index1)
