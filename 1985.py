dic={1001:1.50,1002:2.50,1003:3.50,1004:4.50,1005:5.50}
n=int(input())
SUM=0
for i in range(n):
    a=input().strip()
    list1=a.split()
    SUM+=(dic[int(list1[0])]*int(list1[1]))
print('{:.2f}'.format(SUM))
