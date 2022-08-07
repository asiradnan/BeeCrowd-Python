a=input()
list1=[int(i) for i in input().split()]
two=0
three=0
four=0
five=0
for j in list1:
    if j%2==0:
        two+=1
    if j%3==0:
        three+=1
    if j%4==0:
        four+=1
    if j%5==0:
        five+=1
print(two,'Multiplo(s) de 2')
print(three,'Multiplo(s) de 3')
print(four,'Multiplo(s) de 4')
print(five,'Multiplo(s) de 5')
