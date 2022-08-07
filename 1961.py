ui=input().strip()
one=ui.split()
imp=int(one[0])
uii=input().strip()
two=uii.split()
list1=[int(i) for i in two]
for j in range(len(list1)-1):
    if abs(list1[j+1]-list1[j])>imp:
        print('GAME OVER')
        flag=False
        break
    else:
        flag=True
if flag:
    print('YOU WIN')
