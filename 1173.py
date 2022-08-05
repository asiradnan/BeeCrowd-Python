a=int(input())
list1=[]
count=1
while count<=10:
    list1.append(a)
    a=a*2
    count+=1
for k in range(len(list1)):
    print(f'N[{k}] = {list1[k]}')
