empty=''
a=int(input())
b=a//100
if 1<=b<=3:
    empty+='C'*b
elif b==4:
    empty+='CD'
elif b==5:
    empty+='D'
elif 6<=b<=8:
    empty+='D'
    empty+='C'*(b-5)
elif b==9:
    empty+='CM'
a=a%100
b=a//10
if 1<=b<=3:
    empty+='X'*b
elif b==4:
    empty+='XL'
elif b==5:
    empty+='L'
elif 6<=b<=8:
    empty+='L'
    empty+='X'*(b-5)
elif b==9:
    empty+='XC'
a=a%10
b=a//1
if 1<=b<=3:
    empty+='I'*b
elif b==4:
    empty+='IV'
elif b==5:
    empty+='V'
elif 6<=b<=8:
    empty+='V'
    empty+='I'*(b-5)
elif b==9:
    empty+='IX'
print(empty)
