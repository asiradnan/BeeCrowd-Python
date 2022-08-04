a,b,c=[float(i) for i in input().split()]
if (a+b)>c and (b+c)>a and (a+c)>b:
    print('Perimetro =',a+b+c)
else:
    print('Area =',(a+b)*c*.5)
