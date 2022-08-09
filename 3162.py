list1=[]
for i in range(int(input())):
    y=[int(j) for j in input().split()]
    list1.append(y)
for i in range(len(list1)):
    y=1000000000000
    for j in range(len(list1)):
        if j!=i:
            a=list1[i]
            b=list1[j]
            x=(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))**.5
            if x<y:
                y=x
    if y<=20:
        print('A')
    elif 20<y<=50:
        print('M')
    else:
        print('B')
