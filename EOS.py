num1=int(input("Enter the Starting Number :"))
num2=int(input("Enter the Limit :"))
se=so=0
est=ost=""
for i in range(num1,num2+1):
    if ((i%2)==0):
        est=est+str(i)+'+'
        se+=i
    else:
        ost=ost+str(i)+'+'
        so+=i
print(est,"Even Sum is",se)
print(ost,"Odd Sum is",so)
    
