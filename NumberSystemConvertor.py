print("Enter Decimal Number:")
a=int(input())
print("To which Numerial you want to convert?:")
b=int(input())
c='0123456789ABCDEF'
s=''
while a>=b:
    s=(c[a%b])+s
    a=a//b
print(c[a]+s)
