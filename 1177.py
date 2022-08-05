list1=[]
N=int(input())
while True:
    if len(list1)<1000:
        for i in range(N):
            if len(list1)<1000:
                list1.append(i)
    else:
        break
for j in range(len(list1)):
    print(f'N[{j}] = {list1[j]}')
