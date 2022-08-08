a=input()
start=0
for i in range(len(a)):
    if a[i]=='.' or a[i]=='-':
        print(a[start:i])
        start=i+1
    if a[i]=='-':
        print(a[i+1:])
