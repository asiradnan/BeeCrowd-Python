a=['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
b=['TWENTY','THIRTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']

empty=['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELAVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
for i in range(8):
    k=0
    empty.append(b[i])
    while k<9:
        empty.append(b[i]+' '+a[k])
        k+=1
empty.append('ONE HUNDRED')
y=int(input())
for i in range(1000):
    x=len(empty[y-1])
    y=x
print(y)
