input()
a=input().split()
b=[int(i) for i in a]
f=False
if b[0]>b[1]:
    for j in range(len(b)-1):
        if j%2==0:
            if b[j]>b[j+1]:
                continue
            else:
                f=True
                print(0)
                break
        elif j%2==1:
            if b[j]<b[j+1]:
                continue
            else:
                f=True
                print(0)
                break
else:
    for j in range(len(b)-1):
        if j%2==0:
            if b[j]<b[j+1]:
                pass
            else:
                f=True
                print(0)
                break
        elif j%2==1:
            if b[j]>b[j+1]:
                pass
            else:
                f=True
                print(0)
                break
if f==False:
    print(1)
