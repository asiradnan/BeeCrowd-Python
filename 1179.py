even=[]
odd=[]
for i in range(15):
    a=int(input())
    if a%2==0:
        even.append(a)
        if len(even)==5:
            for j in range(5):
                print(f'par[{j}] = {even[j]}')
            even=[]
    else:
        odd.append(a)
        if len(odd)==5:
            for j in range(5):
                print(f'impar[{j}] = {odd[j]}')
            odd=[]
if len(odd)>=1:
    for j in range(len(odd)):
        print(f'impar[{j}] = {odd[j]}')
if len(even)>=1:
    for j in range(len(even)):
        print(f'par[{j}] = {even[j]}')
