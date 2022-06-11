# write a program to find the
#second largest of list of numbers

##enter the limit
##generate you list of nnumbers
##second largest froma list
##--Sort and -2
import random
n=int(input("Enter the limit:"))
num=list()
for i in range(n):
    num.append(int(random.random()*100))
print("The List contents are",num)
num.sort()
print("The Second Largest number is",num[-2])
