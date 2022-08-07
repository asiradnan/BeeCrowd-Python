def inp():
    b=input().split()
    return [b[0]]+b[1].split('=')
def check():
    name=input().split()
    temp=dic[int(name[-2])]
    if name[-1]=='+':
        if temp[0]+temp[1]==temp[2]:
            return 0
        else:
            return name[0]
    if name[-1]=='-':
        if temp[0]-temp[1]==temp[2]:
            return 0
        else:
            return name[0]
    if name[-1]=='*':
        if temp[0]*temp[1]==temp[2]:
            return 0
        else:
            return name[0]
    if name[-1]=='I' or name[-1]=='i':
        if temp[0]+temp[1]!=temp[2] and temp[0]*temp[1]!=temp[2] and temp[0]-temp[1]!=temp[2]:
            return 0
        else:
            return name[0]
empty=[]
dic={}
count=0
T=int(input().strip())
for i in range(T):
    a=inp()
    dic[i+1]=[int(j) for j in a]
for yz in range(T):
    ehm=check()
    if ehm!=0:
        count+=1
        empty.append(ehm)
if len(empty)==0:
    print('You Shall All Pass!')
elif count==T:
    print('None Shall Pass!')
else:
    empty.sort()
    print(' '.join(empty))
