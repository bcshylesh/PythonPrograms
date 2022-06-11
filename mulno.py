##Multiplication table
##input: 5
##output:
##5x1=5
##5x2=10
##....
##5x10=50
n=int(input("Enter the number :"))
##for i in range(1,11):
##    print(n,"X",i,"=",n*i,sep='')

##for i in range(1,n+1):
##    for j in range(1,11):
##        print(i,"X",j,"=",j*i,sep='')

for i in range(1,11):
    for j in range(1,n+1):
        print(j,"X",i,"=",j*i,sep='',end='\t')
    print()
