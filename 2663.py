count=0
list1=[]
a=int(input())
b=int(input())
for i in range(a):
    list1.append(int(input()))
list1.sort(reverse=True)
last=list1[b-1]
for j in range(b,len(list1)):
    if list1[j]==last:
        count+=1
print(count+b)
