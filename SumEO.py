#Sum of Even & Odd Numbers within the range
num1=int(input("Enter the Starting Number :"))
num2=int(input("Enter the Limit :"))
s=0
if ((num1%2)==0):
    stno=num1+1

for i in range(stno,num2,2):
    print(i,end='+')
    s+=i # s=s+i
if ((num2%2)==0):
    print("=",s)
else
    print(num2,"=",s+num2)
