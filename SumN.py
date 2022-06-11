##Sum of N numbers
##input : 5
##output : 1+2+3+4+5=15
s=0
n=int(input("Enter the Limit :"))
for i in range(1,n):
    print(i,end='+')
    s+=i # s=s+i
print(n,"=",s+n)
