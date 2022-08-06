f=False
count=0
SUM=0
while count<3:
    a=input()
    if a=='caw caw' and f==False:
        f=True
        count+=1
        print(SUM)
        SUM=0
    elif a=='caw caw' and f==True:
        count+=1
        print(0)
    else:
        f=False
        a=a.replace('-','0')
        a=a.replace('*','1')
        if a=='000':
            SUM+=(0)
        elif a=='001':
            SUM+=(1)
        elif a=='010':
            SUM+=(2)
        elif a=='011':
            SUM+=(3)
        elif a=='100':
            SUM+=(4)
        elif a=='101':
            SUM+=(5)
        elif a=='110':
            SUM+=(6)
        else:
            SUM+=(7)
