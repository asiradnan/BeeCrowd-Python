a=int(input())
main=[]
for i in range(a+1):
    b=[int(j) for j in input().split()]
    main.append(b)
for row in range(len(main)-1):
    empty=''
    for col in range(len(main[row])-1):
        if main[row][col]+main[row][col+1]+main[row+1][col]+main[row+1][col+1]>=2:
            empty+='S'
        else:
            empty+='U'
    print(empty)    
