#Search an element from a list of
#numbers entered by the user
import random
n=int(input("Enter the Limit :"))
num=[]  #num=list() Creating an Empty List
for i in range(n):
    num.append(int(random.random()*100))
print("The list is",num)
##read an element to searrch
##seach the element in the list
##if found print found at position
##                         else print not found
se=int(input("Enter the Element to be searched:"))
if (num.count(se)==0):
    print(se,"Not found in the List")
else:
    print(se, "is found at",num.index(se)+1,"position")

