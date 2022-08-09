main=[0,0]
um=[0,0]
for i in range(int(input())):
    a=input().split()
    if a[0]=='chuva':
        if um[0]==0:
            main[0]+=1
        else:
            um[0]-=1
        um[1]+=1
    if a[1]=='chuva':
        if um[1]==0:
            main[1]+=1
        else:
            um[1]-=1
        um[0]+=1
print(main[0],main[1])
