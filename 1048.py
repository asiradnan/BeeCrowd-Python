salary=float(input())
if 0<salary<=400:
    print('Novo salario: {:.2f}'.format(salary+(salary*.15)))
    print('Reajuste ganho: {:.2f}'.format(salary*.15))
    print('Em percentual: 15 %')
elif 400<salary<=800:
    print('Novo salario: {:.2f}'.format(salary+(salary*.12)))
    print('Reajuste ganho: {:.2f}'.format(salary*.12))
    print('Em percentual: 12 %')
elif 800<salary<=1200:
    print('Novo salario: {:.2f}'.format(salary+(salary*.1)))
    print('Reajuste ganho: {:.2f}'.format(salary*.1))
    print('Em percentual: 10 %')
elif 1200<salary<=2000:
    print('Novo salario: {:.2f}'.format(salary+(salary*.07)))
    print('Reajuste ganho: {:.2f}'.format(salary*.07))
    print('Em percentual: 7 %')
elif 2000<salary:
    print('Novo salario: {:.2f}'.format(salary+(salary*.04)))
    print('Reajuste ganho: {:.2f}'.format(salary*.04))
    print('Em percentual: 4 %')
