alcohol=0
diesel=0
gasoline=0
while True:
    a=int(input())
    if a==1:
        alcohol+=1
    elif a==3:
        diesel+=1
    elif a==2:
        gasoline+=1
    elif a==4:
        break
print("MUITO OBRIGADO")
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gasoline}')
print(f'Diesel: {diesel}')
