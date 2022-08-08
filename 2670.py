list1=[]
for i in range(3):
    list1.append(int(input().strip()))
list2=[]
list2.append(list1[1]*2 + list1[2]*4)
list2.append(list1[0]*2 + list1[2]*2)
list2.append(list1[0]*4 + list1[1]*2)
list2.sort()
print(list2[0])
