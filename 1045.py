list1=[float(i) for i in input().split()]
list1.sort(reverse=True)
A,B,C=list1
if A >= (B + C):
    print('NAO FORMA TRIANGULO')
elif A**2 == (B**2 + C**2):
    print('TRIANGULO RETANGULO')
elif A**2 > (B**2 + C**2):
    print('TRIANGULO OBTUSANGULO')
elif A**2 < (B**2 + C**2):
    print('TRIANGULO ACUTANGULO')
if A**2 == B**2 == C**2:
    print('TRIANGULO EQUILATERO')
elif (A==B and A!=C) or (A==C and A!=B) or (C==B and A!=C):
    print('TRIANGULO ISOSCELES')
