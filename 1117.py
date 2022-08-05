list1=[]
while True:
    a=float(input())
    if 0<=a<=10:
        list1.append(a)
    else:
        print('nota invalida')
    if len(list1)==2:
        print('media = {:.2f}'.format((list1[0]+list1[1])/2))
        break
