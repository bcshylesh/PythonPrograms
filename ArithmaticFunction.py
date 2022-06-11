## program to find result of arithmatic operations
## using user defined functions   +, -,*,/,%,**
##
##input : 2 numbers , opration
##output : Result depending on operation
##operation: functions, conditional stmts


def add2(x,y):
    print("The sum is",x+y)
def sub2(x,y):
    print("The Difference is",x-y)
def mul2(x,y):
    print("The product is",x*y)

a=int(input("Enter the first number :"))
b=int(input("Enter the Second number :"))
c=input("Enter the operrator (+, -,*,/,%,**) :")
if (c=="+"):
    add2(a,b)
elif(c=="-"):
    sub2(a,b)
elif(c=="*"):
    mul2(a,b)
