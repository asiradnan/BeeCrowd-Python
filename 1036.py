A,B,C=[float(i) for i in input().split()]
D=(B**2)-(4*A*C)
if D>=0 and A!=0:
    print('R1 = {:.5f}'.format((-B+(D**.5))/(2*A)))
    print('R2 = {:.5f}'.format((-B-(D**.5))/(2*A))) 
else:
    print('Impossivel calcular')
