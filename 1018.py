N=int(input())
print(N)
a=N//100
print(a,'nota(s) de R$ 100,00')
b=N%100
c=b//50
print(c,'nota(s) de R$ 50,00')
d=b%50
e=d//20
print(e,'nota(s) de R$ 20,00')
f=d%20
g=f//10
print(g,'nota(s) de R$ 10,00')
h=f%10
i=h//5
print(i,'nota(s) de R$ 5,00')
j=h%5
k=j//2
print(k,'nota(s) de R$ 2,00')
print(j%2,'nota(s) de R$ 1,00')
