input()
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
count=0
for j in a:
    if j not in b:
        count+=1
print(count)
