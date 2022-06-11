#sorting a list of numbers entered by the user
##    Read the limit
##    create a empty list
##    Loop through the limit
##    append method of list
##    use sort method of list
##    print  the list
n=int(input("Enter the Limit :"))
num=[]  #num=list() Creating an Empty List
print("Enter the elements :")
for i in range(n):
    b=input()
    num.append(b)
print("The list is",num)
num.sort()
print("The Sorted list is",num)
