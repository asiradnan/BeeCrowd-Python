SUM=0
for i in range(int(input())):
    a=input().lower()
    if 'cd' not in a:
        SUM+=1
print(SUM)
