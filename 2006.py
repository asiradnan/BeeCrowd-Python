T=int(input())
count=0
list1=[int(i) for i in input().split()]
for j in list1:
    if j==T:
        count+=1
print(count)
