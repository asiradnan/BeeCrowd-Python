list1=[]
list2=[]
for i in range(1,int(input())+1):
    list1.append(i)
for j in range(int(input())):
    list2.append(int(input()))
count=0
for k in list1:
    if k not in list2:
        count+=1
print(count)
