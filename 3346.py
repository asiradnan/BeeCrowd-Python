a=[float(i) for i in input().split()]
b=100
b+=b*(a[0]/100)
b+=b*(a[1]/100)
print('{0:.6f}'.format(b-100))
