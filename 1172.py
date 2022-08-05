list1=[]
for i in range(10):
    list1.append(int(input()))
for j in range(len(list1)):
    if list1[j]<=0:
        list1[j]=1
for k in range(len(list1)):
    print(f'X[{k}] = {list1[k]}')
