xy=input()
list1=xy.split()
X=int(list1[0])
Y=int(list1[1])+1
for i in range(1,Y):
    if i%(X)!=0:
        print(i,end=' ')
    else:
        print(i)
