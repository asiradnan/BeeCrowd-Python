a=[int(i) for i in input().split()]
r=a[0]
c=a[1]
main=[]
for j in range(r):
    list1=[int(k) for k in input().split()]
    main.append(list1)
def func():
    for row in range(1,len(main)-1):
        for col in range(1,len(main[row])-1):
            if main[row][col]==42:
                if main[row][col+1]==main[row][col-1]==main[row+1][col-1]==main[row+1][col]==main[row+1][col+1]==main[row-1][col-1]==main[row-1][col]==main[row-1][col+1]==7:
                    return row+1,col+1
f=func()
if f==None:
    print('0 0')  
else:
    print(f[0],f[1])
