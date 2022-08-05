list1=[0,1]
x=0
y=1
while True:
    z=x+y
    if len(list1)<61:
        list1.append(z)
    else:
        break
    x=y
    y=z
T=int(input())
for i in range(T):
    N=int(input())
    print(f'Fib({N}) = {list1[N]}')
