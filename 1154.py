count=0
age=0
while True:
    a=int(input())
    if a>=0:
        count+=1
        age+=a
    else:
        break
print('{:.2f}'.format(age/count))
