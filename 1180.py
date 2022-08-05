N=int(input())
a=input()
list1=a.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
list2=list1.copy()
list2.sort()
print('Menor valor:',list2[0])
print('Posicao:',list1.index(list2[0]))
