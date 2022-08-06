bazinga=['tesoura papel','papel pedra','pedra lagarto','lagarto Spock','Spock tesoura','tesoura lagarto','lagarto papel','papel Spock','Spock pedra','pedra tesoura']
rajinga=['papel tesoura','pedra papel','lagarto pedra','Spock lagarto','tesoura Spock','lagarto tesoura','tesoura pedra','pedra Spock','Spock papel','papel lagarto']
for i in range(int(input())):
    a=input().strip()
    b=a.split()
    if a in bazinga:
        print(f'Caso #{i+1}: Bazinga!')
    elif a  in rajinga:
        print(f'Caso #{i+1}: Raj trapaceou!')
    else:
        print(f'Caso #{i+1}: De novo!')
