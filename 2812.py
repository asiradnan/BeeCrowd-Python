empty=''
for tan in range(int(input())):
    even=[]
    #empty=''
    x=int(input())
    for i in range(1,x+1):
        if i%2==1:
            even.append(i)
    print(even)
    if (len(even))%2==0:
        f=True
    else:
        f=False
    even2=even[int(len(even)/2):]
    even2=sort(reverse=True)
    print(even2)
    if f:
        for xyz in range(len(even2)):
            empty+=(str(even[xyz]))+str(even2[xyz])
    print(empty)
