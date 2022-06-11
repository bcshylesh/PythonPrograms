#Generate numbers between the range
#input : 2 numbers , First ; staring
#                   second :End point
# out : Print the series from first to second
# Eg: 3,7
#  O/p : 3 4 5 6 7
num1=int(input("Enter the Starting Number :"))
num2=int(input("Enter the Limit :"))
for i in range(num1,num2+1):
    print(i,end=',')
#3,4,5,6,7,
    
for i in range(num1,num2):
    print(i,end=',')
print(num2)
#3,4,5,6,7
