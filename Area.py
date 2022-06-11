##write a program to fins the areaof
##circle, square, rectangle,traingle using functions
##
##circle - pi r * r
##square --a *a
##rectangle - a*b
##triangle a*b /2
import math
def areaCircle():
    r=int(input("Enter the radius :"))
    a=math.pi * r * r
    print("Area is ",a)
def areaSquare():
    r=int(input("Enter the side :"))
    a=r * r
    print("Area is ",a)
def areaRectangle():
    l=int(input("Enter the legnth :"))
    b=int(input("Enter the breadth :"))
    a=l * b
    print("Area is ",a)
def areaTriangle():
    l=int(input("Enter the legnth :"))
    b=int(input("Enter the breadth :"))
    a=0.5 * l * b
    print("Area is ",a)
while(1):

    print("1 - Area of Circle")
    print("2 - Area of Square")
    print("3 - Area of Rectangle")
    print("24 - Area of Triangle")    
    print("5 - Exit")
    ch=int(input("Enter your choice :"))
    if(ch==1):
        areaCircle()
    elif(ch==2):
        areaSquare()
    elif(ch==3):
        areaRectangle()
    elif(ch==4):
        areaTriangle()
    elif(ch==5):
        exit()
    else:
        print("Invalid Choice")
