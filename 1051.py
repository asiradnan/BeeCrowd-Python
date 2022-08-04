salary=float(input())-2000
tax=0
if salary>2500:
    x=salary-2500
    salary-=x
    tax+=x*.28
if 1000<salary<=2500:
    x=salary-1000
    salary-=x
    tax+=x*.18
if 0<salary<=1000:
    tax+=salary*.08
if tax!=0:
    print('R$ {:.2f}'.format(tax))
else:
    print('Isento')
