a=[int(i) for i in input().split()]
H,E,A,O,W,X=tuple(a)
if H+E+A+X>=O+W:
  print('Middle-earth is safe.')
else:
  print('Sauron has returned.')
