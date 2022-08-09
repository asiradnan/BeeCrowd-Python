search=[]
a=[int(i) for i in input().split()]
for i in range(a[0]):
    search.append(input().lower())
fruits=[]
for i in range(a[1]):
    fruits.append(input().lower())
def check(i):
    x=i[::-1]
    for j in fruits:
        if i in j or x in j:
            return True
    return False
for i in search:
    f=check(i)
    if f==False :
        print(f'Sheldon detesta a fruta {i}')
    else:
        print(f'Sheldon come a fruta {i}')  
