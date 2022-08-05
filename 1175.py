list1=[]
for i in range(20):
    list1.append(int(input()))
count=0
while count<(len(list1)/2):
    list1[count],list1[len(list1)-count-1]=list1[len(list1)-count-1],list1[count]
    count+=1
for k in range(len(list1)):
    print(f'N[{k}] = {list1[k]}')
