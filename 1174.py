list1=[]
for i in range(100):
    list1.append(float(input()))
for k in range(len(list1)):
    if list1[k]<=10:
        print('A[{0:}] = {1:.1f}'.format(k,list1[k]))
