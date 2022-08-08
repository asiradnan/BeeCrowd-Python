print('-'*39)
print('|  decimal  |  octal  |  Hexadecimal  |')
print('-'*39)
for i in range(16):
    a=oct(i)
    b=hex(i)
    print('|{0:>7}    |{1:^9}|{2:^15}|'.format(i,a[2:],b[2:].upper()))
print('-'*39)
