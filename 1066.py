positive=0
even=0
negative=0
odd=0
for i in range(5):
    a=int(input())
    if a%2==0:
        even+=1
    if a%2==1:
        odd+=1
    if a>0:
        positive+=1
    if a<0:
        negative+=1
print(even,'valor(es) par(es)')
print(odd,'valor(es) impar(es)')
print(positive,'valor(es) positivo(s)')
print(negative,'valor(es) negativo(s)')
