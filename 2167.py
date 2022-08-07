hudai=input()
list1=input().split()
list2=[int(i) for i in list1]
count=0
for j in range(len(list2)-1):
    if list2[j]>list2[j+1]:
        count=j+2
        break
print(count)
