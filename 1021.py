x=float(input())
print('NOTAS:')
y=x//100
print(f'{int(y)} nota(s) de R$ 100.00')
x=x%100
a=x//50
print(f'{int(a)} nota(s) de R$ 50.00')
x=x%50
b=x//20
print(f'{int(b)} nota(s) de R$ 20.00')
x=x%20
c=x//10
print(f'{int(c)} nota(s) de R$ 10.00')
x=x%10
d=x//5
print(f'{int(d)} nota(s) de R$ 5.00')
x=x%5
e=x//2
print(f'{int(e)} nota(s) de R$ 2.00')
print('MOEDAS:')
x=x%2
f=x//1
print(f'{int(f)} moeda(s) de R$ 1.00')
x=x%1
g=x//.5
print(f'{int(g)} moeda(s) de R$ 0.50')
x=x%.5
h=x//.25
print(f'{int(h)} moeda(s) de R$ 0.25')
x=x%.25
i=x//.1
print(f'{int(i)} moeda(s) de R$ 0.10')
x=x%.1
x=x*100
j=(x//5)
print(f'{int(j)} moeda(s) de R$ 0.05')
x=x%5
print(f"{int(x)} moeda(s) de R$ 0.01")
