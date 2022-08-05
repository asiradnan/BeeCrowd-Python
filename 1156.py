S=1
j=2
for i in range(3,40,2):
    S+=(i/j)
    j=j*2
print('{:.2f}'.format(S))
