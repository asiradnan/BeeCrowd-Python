ave={'carnivoro':'aguia','onivoro':'pomba'}
mamifero={'onivoro':'homem','herbivoro':'vaca'}
vertebrado={'ave':ave,'mamifero':mamifero}
inseto={'hematofago':'pulga','herbivoro':'lagarta'}
anelideo={'hematofago':'sanguessuga','onivoro':'minhoca'}
invertebrado={'inseto':inseto,'anelideo':anelideo}
a=input()
b=input()
c=input()
if a=='vertebrado':
    print(vertebrado[b][c])
else:
    print(invertebrado[b][c])
